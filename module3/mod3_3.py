namelist = ["David", "Peter", "Julia"]
for name in ["David", "Peter", "Julia"]:
    print(name)

for i in range(10):
    print(i)
for i in range(3,6):
    print(i)

#Skriver ut en multiplikationstabell från 1 till 10.
for i in range(1, 11):
  for j in range (1,11):
    print ("%2d"%(i*j), end = "  ")
  print()

#Här använder vi listor i varandra och bygger upp en matris istället.
multiplikationstabell = []
HÖGSTA_TALET = 6  #Här kan vi ändra om vi vill minska/utöka vilka tal som ska vara med i tabellen
for i in range(1,HÖGSTA_TALET + 1):
  produktlista = []  #Vår inre lista där vi kommer lagra vår resultat
  for j in range(1,HÖGSTA_TALET + 1):
    produkt = i*j 
    produktlista.append(produkt)
  multiplikationstabell.append(produktlista)


#Här skriver vi ut vår matris
for i in range(len(multiplikationstabell)):
  print("Multiplikationstabell för " + str(i+1) + ":", end= " ")
  for j in multiplikationstabell[i]:
    print(j, end = " ")
  print()#Så att vi får nästa utskrift på ny rad
