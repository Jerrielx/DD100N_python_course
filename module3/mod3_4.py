emptyDictonary = {}
myDictionary = {"key":"data"} #nyckeln blir här "key" och värdet "data"
print(myDictionary)
ageDict = {"Svea":26 , "Saga":32, "Ture":20}
print(ageDict)
age = ageDict["Svea"] 
print(age)
ageDict["Svea"] = 27 # ändra value i befintlig nyckel
ageDict["Elsa"] = 22 # lägga till ny nyckel/värde
print(ageDict)
del ageDict["Svea"] # tar bort nycket-värde par
print(ageDict)
nameList = ageDict.keys()
print(nameList)

månader = {"jan":31, "feb":28, "mar":31, "apr":30,
"maj":31, "jun":30, "jul":31, "aug":31, "sep":30,
"okt":31, "nov":30, "dec":31} 

vald_månad = input("Vilken månad vill du veta antalet dagar i?")

if vald_månad in månader.keys():  #Om den valda månden är en nyckel i hashtabellen månader
  print(vald_månad, "har", månader[vald_månad], "antal dagar.")

print("\nHela året ser ut så här:")
for månad in månader.keys(): #Går igenom varje nyckel och skriver ut nyckeln och värdet
  print(månad, "har", månader[månad], "antal dagar.")
