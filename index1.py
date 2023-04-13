# Vigenère-Entschlüsselung in Python

# Gegebener verschlüsselter Text und Schlüssel
verschluesselt = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
schluessel = "PALIMPSEST"

# Funktion zur Entschlüsselung des Vigenère-Verschlüsselungsalgorithmus
def vigenere_entschluesselung(verschluesselt, schluessel):
    # Umwandlung von Groß- zu Kleinbuchstaben
    verschluesselt = verschluesselt.lower()
    schluessel = schluessel.lower()
    # Initialisierung der Entschlüsselungszeichenkette
    entschluesselt = ""
    # Berechnung der Entschlüsselung durch Zählen der Schlüsselzeichen
    for i in range(len(verschluesselt)):
        verschluesselt_char = verschluesselt[i]
        schluessel_char = schluessel[i % len(schluessel)]
        # Umwandlung von Buchstaben in ASCII-Werte
        verschluesselt_num = ord(verschluesselt_char) - 97
        schluessel_num = ord(schluessel_char) - 97
        # Entschlüsselung der ASCII-Werte
        entschluesselt_num = (verschluesselt_num - schluessel_num) % 26
        # Umwandlung der ASCII-Werte in Buchstaben
        entschluesselt_char = chr(entschluesselt_num + 97)
        # Hinzufügen des entschlüsselten Zeichens zur Entschlüsselungszeichenkette
        entschluesselt += entschluesselt_char
    return entschluesselt

# Anwenden der Vigenère-Entschlüsselung auf den verschlüsselten Text mit dem gegebenen Schlüssel
entschluesselt = vigenere_entschluesselung(verschluesselt, schluessel)

# Ausgabe des entschlüsselten Textes
print("Entschlüsselter Text:", entschluesselt)
