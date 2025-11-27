# File: Inlämningsuppgift1.py
# Author: Jerry Cheung
# Date: 21/11/2025
# Course: DD100N
# Description:  Konvertering av enheter

print("Välkommen till Konverteraren!")
val = 0
while True:
    print("Välj en av följande konverteringar")
    print("1. Grader Celsius till grader Fahrenheit")
    print("2. Meter till amerikanska mil")
    print("3. Liter till gallon")
    print("4. Avsluta")
    val = int(input("Vad väljer du?: "))
    if val == 1:
        # celsius till fahrenheit
        temperatur = float(input("Ange grader i Celsius: "))
        print(f"{temperatur:g}", "grader Celsius motsvarar", "%.2f"%(temperatur*1.8+32), "grader Farenheit")
    elif val == 2:
        # meter till mil
        distans = float(input("Ange distans i meter: "))
        print(f"{distans:g}", "meter motsvarar", "%.2f"%(distans/1609.3), "mil")
    elif val == 3:
        # liter till gallon
        volym = float(input("Ange volymen i liter: "))
        print(f"{volym:g}", "liter motsvarar", "%.2f"%(volym/3.785), "gallon.")
    elif val == 4:
        # exit loop
        break
    else:
        # not available input
        print("fel menyval. Ange 1-4")
print("Välkommen åter!")
