# Course: DD100N
# Author: Jerry Cheung
# Date: 27/11/2025
# File: Uppg1.py
# Description:  tal = [4, 16, 2, 81, 43, 5, 80, 13]
# Skriv en kod som summerar alla element i listan tal och skriver ut summan.

tal = [4, 16, 2, 81, 43, 5, 80, 13]
sum = 0
for i in range(len(tal)):
    sum += tal[i]
    print(tal[i], end=" ")
print()
print(sum)