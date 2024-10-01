import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, MaxNLocator

# LaTeX-Schriftart aktivieren
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Konvertiere cm in inch
cm_to_inch = 1 / 2.54



x_min = -2
x_max = 2 # Maximaler x-Wert
y_min = -4
y_max = 4 # Maximaler y-Wert

grid_spacing_x = 1
grid_spacing_y = 1


# Die Breite der x-Achse in cm beträgt 3 cm und die Höhe der y-Achse 5 cm
axis_width_cm = x_max - x_min # 3 cm Breite
axis_height_cm = y_max - y_min  # 5 cm Höhe
axis_width_inch = axis_width_cm * cm_to_inch  # 3 cm in inch
axis_height_inch = axis_height_cm * cm_to_inch  # 5 cm in inch

# Bestimme die Ränder (Platz für Beschriftungen und Labels)
margin_inch = 0.8  # 0.8 inch Rand um die Achsen (für Achsentitel, Labels etc.)

# Berechne die Gesamtgröße der Figur, inklusive der Ränder
fig_width_inch = axis_width_inch + 2 * margin_inch
fig_height_inch = axis_height_inch + 2 * margin_inch

# Erstelle die Figur
fig = plt.figure(figsize=(fig_width_inch, fig_height_inch))
ax = fig.add_axes([margin_inch / fig_width_inch, 
                   margin_inch / fig_height_inch, 
                   axis_width_inch / fig_width_inch, 
                   axis_height_inch / fig_height_inch])

# Erzeuge die Daten und die Funktion
x = np.linspace(x_min, x_max, 1000)
y1 = x * x * x # Plot (a)

# Plotten der Funktion
ax.plot(x, y1, 'r')

# Setze die Limits so, dass die Achsen 3 cm und 5 cm lang sind
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])


# X-Achse
ax.xaxis.set_major_locator(MultipleLocator(grid_spacing_x))  # Hauptticks
ax.xaxis.set_minor_locator(AutoMinorLocator(2))  # Hilfsticks (jede zweite Hauptlinie)

# Y-Achse
ax.yaxis.set_major_locator(MultipleLocator(grid_spacing_y))  # Hauptticks
ax.yaxis.set_minor_locator(AutoMinorLocator(2))  # Hilfsticks (jede zweite Hauptlinie)

# Zeichne den Plot, um die Ticks und Labels korrekt zu generieren
plt.draw()

# Hole die aktuell gesetzten Ticks
xticks = ax.get_xticks()
yticks = ax.get_yticks()

# Setze die Labels manuell, wobei das letzte Label ausgeblendet wird (HOKUSPOKUS)
xtick_labels = [item.get_text() for item in ax.get_xticklabels()]
xtick_labels[-2] = ''  # Letztes X-Label entfernen
ax.set_xticklabels(xtick_labels)

ytick_labels = [item.get_text() for item in ax.get_yticklabels()]
ytick_labels[-2] = ''  # Letztes Y-Label entfernen
ax.set_yticklabels(ytick_labels)

# Füge das Gitter hinzu
ax.grid(which='both')  # Beide, major und minor Ticks

# Achsenpfeile und Beschriftungen
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Die Pfeile
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=7)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=7)


# Setze die Achsenbeschriftungen dort, wo die letzte Zahl (3 und 5) wäre
ax.text(x_max, -0.2, r'$U \, [\mathrm{V}]$', verticalalignment='top', horizontalalignment='center', fontsize=12)
ax.text(-0.2, y_max, r'$I \, [\mathrm{A}]$', verticalalignment='center', horizontalalignment='right', fontsize=12, rotation=0)


# Speichere den Plot ohne unnötige Ränder
plt.savefig('plot.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
plt.show()
