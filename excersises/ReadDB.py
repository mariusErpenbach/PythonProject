# Öffnen und Lesen der Datei
with open("Datenbank.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)

# Schreiben in die Datei
newText = "whatever"
with open("Datenbank.txt", "w") as file:
    file.write(newText)