# File: Jerry_Cheung_1.py
# Author: Jerry Cheung
# Date: 26/8/2025
# Course: DD100N
# Description:  Presentation of me

MY_NAME = "Jerry"
my_age = 31
my_shoe_size = 43.5
nr_of_pet = 0
days_per_year = 365.2422
my_age_in_days = my_age * days_per_year
steam_game_hours = 4405
hours_per_day = 24
steam_game_days = steam_game_hours/hours_per_day

print("Hej!")
print("Jag heter", MY_NAME, "och är", my_age, "gammal.", end=" ")
print("Jag har nr", my_shoe_size, "i skostorlek.")
print("Jag har " + str(nr_of_pet) + " husdjur.")
print("Min ålder, ", str(my_age), " år, motsvar en ålder på hela", end=" ")
print(int(my_age_in_days), "dagar (inräknat skottår).")
print("Jag har " + str(steam_game_hours) + " timmar på ett spel", end=" ")
print("som motsvarar", int(steam_game_days), "dagar.")
