namnlista = [] #skapar tom lista

namn1 = "Erik"
namn2 = "Jessica"
namnlista.append(namn1)
namnlista.append(namn2)
print(namnlista)
print(namnlista[0])


bokstavslista = ["A", "B", "C", "D"]
print(bokstavslista) # visar: ['A', 'B', 'C', 'D']
bokstavslista.remove("D")
print(bokstavslista) # visar: ['B', 'C', 'D']
bokstavslista.append("D")
bokstavA = bokstavslista.pop(3)
print(bokstavA) # visar: D
print(bokstavslista) # visar: ['A', 'B', 'C']
del bokstavslista[2] # tar bort index2 från lista
namnlista = ["A", "B", "C", "D"]
print(namnlista[2:]) # visar: ['C', 'D']
