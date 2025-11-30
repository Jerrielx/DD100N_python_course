# Program:  TIDAA
# Course:   DD100N
# Author:   Jerry Cheung
# Date:     27/11/2025
# File:     Jerry_Cheung3.py
# Description:  Inlämningsuppgift 3

print("Välkommen till programmet som håller ordning på längdhoppen!")
print("Programmet antar att du har 3 elever och varje elev gör 3 hopp.")
print("Vi börjar med att skriva in alla elever och längden på deras hopp.")
ANTAL_ELEVER = 3
ANTAL_HOPP = 3
elever_längdhopp = {}
for i in range(ANTAL_ELEVER):
    elev = input("Namn på elev: ")
    längdhopp = []
    for j in range(ANTAL_HOPP):
        print("Skriv längden på hopp nr" , (j+1) ,end = "")
        hopp = float(input(": "))
        längdhopp.append(hopp)
    elever_längdhopp[elev] = längdhopp

#pls aprove my pr!
select = 0
while select != 3:
    print("\n1. Visa all resultat")
    print("2. Visa längsta hopp för varje elev")
    print("3. Avsluta program")
    select = int(input("Välj en siffra mellan 1-3: "))
    if select == 1:
        for elev in elever_längdhopp:
            print(elev, "hoppade" , end = " ")
            for hopp in elever_längdhopp[elev]:
                print("%.2f"%(hopp), end = " ")
            print("meter.")
    elif select == 2:
        for elev in elever_längdhopp:
            max = elever_längdhopp[elev][0]
            for hopp in elever_längdhopp[elev]:
                if hopp > max:
                    max = hopp
            print(elev, "hoppade som längst", "%.2f"%(max), "meter.")
    elif select == 3: break
    else :
        print("Fel input. Välj mellan 1-3")
print("Välkommen åter!")