import matplotlib.pyplot as plt

# Daten für den Milchmarkt
angebot_ohne_quote = [10, 20, 30, 40, 50]  # Menge an Milch ohne Quote
nachfrage = [50, 40, 30, 20, 10]  # Nachgefragte Menge Milch
angebot_mit_quote = [8, 16, 24, 32, 40]  # Menge an Milch mit Quote

# Milchpreise
milchpreis_ohne_quote = [2, 3, 4, 5, 6]  # Milchpreise ohne Quote
milchpreis_mit_quote = [3, 4.5, 6, 7.5, 9]  # Milchpreise mit Quote

# Plot erstellen
plt.figure(figsize=(8, 6))

# Angebots- und Nachfragekurve darstellen
plt.plot(nachfrage, milchpreis_ohne_quote, label='Nachfrage ohne Quote')
plt.plot(nachfrage, milchpreis_mit_quote, label='Nachfrage mit Quote')

# Angebotskurve ohne Quote darstellen
plt.plot(angebot_ohne_quote, milchpreis_ohne_quote, label='Angebot ohne Quote')

# Angebotskurve mit Quote darstellen
plt.plot(angebot_mit_quote, milchpreis_mit_quote, label='Angebot mit Quote')

# Gleichgewichtspunkte markieren
gleichgewicht_ohne_quote = (30, 4)
gleichgewicht_mit_quote = (26.7, 6.5)
plt.scatter(*gleichgewicht_ohne_quote, color='r', marker='o', label='Gleichgewicht ohne Quote')
plt.scatter(*gleichgewicht_mit_quote, color='g', marker='o', label='Gleichgewicht mit Quote')

# Achsenbeschriftung
plt.xlabel('Menge Milch')
plt.ylabel('Milchpreis')

# Titel und Legende hinzufügen
plt.title('Wirkung der Milchquote auf den Milchmarkt')
plt.legend()

# Grid anzeigen
plt.grid(True)

# Plot anzeigen
plt.show()
