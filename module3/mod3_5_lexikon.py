#Ett program som fungerar som ett lexikon där det svenska ordet är nyckel och värdet är en lista med översättningar på engelska, tyska och italienska.

lexikon = {} #En tom hashtabell, som vi sedan kommer fylla på med vår ord och deras översättningar
nycklar =["glass","hej","måndag"]
värden = [] #En tom lista med värden, som vi sedan kommer fylla på
glassÖversättning = ["ice cream","Eis","gelato"]
värden.append(glassÖversättning)
hejÖversättning = ["hi","hallo","ciao"]
värden.append(hejÖversättning)
måndagÖversättning = ["Monday","Montag","lundi"]
värden.append(måndagÖversättning) #Nu ser listan ut så här: [['ice cream', 'Eis', 'gelato'], ['hi', 'hallo', 'ciao'], ['Monday', 'Montag', 'lundi']]

for i in range(len(nycklar)):
  lexikon[nycklar[i]]=värden[i] #Här lägger vi till ett element i vår hashtabell, första gången for-slinga körs kommer i=0 och vi kommer lägga till lexikon["glass"]=['ice cream', 'Eis', 'gelato']
print("Hej och välkommen till lexikonet! Följande ord finns det översättningar på: ")
for nyckel in lexikon.keys():
  print(nyckel)
print("språken du kan välja att översätt till är engelska, tyska och italienska")

val = 0
while val != 3:
  print("\n1. Översätt ett ord \n2. Lägg till ett ord \n3. Avsluta")
  val = int(input("Välj en siffra 1-3: \n"))
  if val == 1: # Översätta ett ord
    svensktOrd = input("Vilket ord vill du översätta? ")
    språk = input("Vilket språk vill du översätta till? ")
    if svensktOrd in lexikon.keys():
      if språk[0] == "e": #Om första bosktaven på språk är e är vi ute efter det engelska ordet
        översättning = lexikon[svensktOrd][0] #Här tar vi fram det ord som finns på index 0, i listan med värdet, med den givna nyckeln
        print(svensktOrd, "översätts till", översättning)
      elif språk[0] == "t":
        översättning = lexikon[svensktOrd][1]
        print(svensktOrd, "översätts till", översättning)
      elif språk[0] == "i":
        översättning = lexikon[svensktOrd][2]
        print(svensktOrd, "översätts till", översättning)
      else:
        print("Det språket har vi ingen översättning till.")
                
    else:
      print("Det ordet finns inte lexikonet")
            
  elif val == 2: # lägga till ett ord
    svensktOrd = input("Vilket ord vill du lägga till? ")
    översättningar = [] #Tom lista där vi sedan fyller på med varje värde.
    engelsktOrd = input("Vad heter det på engelska? ")
    översättningar.append(engelsktOrd)
    tysktOrd = input("Vad heter det på tyska? ")
    översättningar.append(tysktOrd)
    italiensktOrd = input("Vad heter det på italienska? ")
    översättningar.append(italiensktOrd)
    lexikon[svensktOrd] = översättningar  #Här lägger vi till ordet i vårt lexikon
    print("Det svenska ordet", svensktOrd, "har lagts till med översättningarna: ")
    for i in range(3):
      print(lexikon[svensktOrd][i], end= " ")
    print() #Skriver bara ut en blankrad

  elif val == 3: #avsluta
    print("Välkommen åter!")

  else:
    print("Tyvärr så skrev du något fel. Försök igen!")

