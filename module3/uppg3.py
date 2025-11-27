# Course: DD100N
# Author: Jerry Cheung
# Date: 27/11/2025
# File: Uppg3.py
# Description: 

# Målet med programmet är att hitta det minsta värdet i en lista med en slinga

värden = [14, 8, 27, 3, 11, 5, 20]

# Anta att det första värdet i listan är det minsta, lagra det i variabeln minsta
minsta = värden[0]

for nummer in värden:
    if nummer < minsta : #här saknas villkoret, hur ska vi veta om vi hittat ett mindre värde?
      minsta =  nummer # Om vi hittat ett mindre värde, uppdatera minsta till det värdet.

print("Det minsta värdet i listan är", minsta) # Skriv ut resultatet