import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, MaxNLocator

# LaTeX-Schriftart aktivieren
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Konvertiere cm in inch
cm_to_inch = 1 / 2.54

# Die Breite der x-Achse in cm beträgt 3 cm und die Höhe der y-Achse 5 cm
axis_width_cm = 3  # 3 cm Breite
axis_height_cm = 5  # 5 cm Höhe
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
x = np.linspace(0, 5, 1000)
y1 = x * x  # Plot (a)

# Plotten der Funktion
ax.plot(x, y1, 'r')

# Setze die Limits so, dass die Achsen 3 cm und 5 cm lang sind
ax.set_xlim([0, 3])
ax.set_ylim([0, 5])

# Setze die Ticks und entferne nur die äußersten Zahlen, nicht die Hilfslinien
ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='upper'))  # Entfernt oberste Haupt-Ticks (Zahlen)
ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='upper'))  # Entfernt oberste Haupt-Ticks (Zahlen)

# Behalte die Hilfslinien bei
ax.xaxis.set_minor_locator(AutoMinorLocator(2))  # Hilfslinien (Minor Ticks)
ax.yaxis.set_minor_locator(AutoMinorLocator(2))  # Hilfslinien (Minor Ticks)

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
ax.text(3, -0.2, r'$U \, [\mathrm{V}]$', verticalalignment='top', horizontalalignment='center', fontsize=12)
ax.text(-0.2, 5, r'$I \, [\mathrm{A}]$', verticalalignment='center', horizontalalignment='right', fontsize=12, rotation=0)


# Speichere den Plot ohne unnötige Ränder
plt.savefig('plot.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
plt.show()
