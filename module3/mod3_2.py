namnlista = ["A", "B", "D", "E"]
namnlista.insert(2,"C") #lägger till på plats nr 2
print(namnlista) # visar: ['A', 'B', 'C', 'D', 'E']

namnlista = ["A", "B", "C", "D"]
listanslängd = len(namnlista)
print(listanslängd) # visar: 4

listaBokstäver = ["B","D", "A", "C"]
listaBokstäver.sort()
print(listaBokstäver) # Visar ['A', 'B', 'C', 'D']
listaBokstäver = ["B","D", "A", "C"]
listaBokstäver.sort(reverse = True)
print(listaBokstäver)   # Visar ['E', 'D', 'C',' B', 'A']

listaBokstäver = ["B","D", "A", "C"]
sorteradLista = sorted(listaBokstäver)
print(sorteradLista)  # Visar ['A', 'B', 'C', 'D']
print(listaBokstäver) # Visar ['B', 'D', 'A', 'C']

namnlista = ["A", "B", "D", "E"]
namnlista.insert(2,"C") #lägger till på plats nr 2
print(namnlista) # visar: ['A', 'B', 'C', 'D', 'E']
listanslängd = len(namnlista)
print(listanslängd) # visar: 5
namnlista.sort(reverse = True)
print(namnlista)   # Visar ['E', 'D', 'C',' B', 'A']
sorteradLista = sorted(namnlista)
print(sorteradLista)  # Visar ['A', 'B', 'C', 'D', 'E']
print(namnlista) # Visar ['E', 'D', 'C',' B', 'A']

lista = [2,1,12,3]
sorterad_lista = sorted(lista)
print(sorterad_lista)
