good = 0
bad = []

current = 1
answer = input(
1. Wat betekent het genotype Aa
A Homozygoot dominant
B Homozygoot recessief
C Heterozygoot
D Geen allelen
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


current = 2
answer = input(
2. Wat betekent homozygoot
A Twee verschillende allelen
B Twee gelijke allelen
C Geen allelen
D Vier allelen
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 3
answer = input(
3. Wat betekent heterozygoot
A Twee verschillende allelen
B Twee gelijke allelen
C Geen genotype
D Alleen recessief
(ABCD)
)
if answer == A
    good += 1
else
    bad.append(current)


current = 4
answer = input(
4. Welk genotype is homozygoot recessief
A AA
B Aa
C aa
D A_
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


current = 5
answer = input(
5. Welk genotype is homozygoot dominant
A AA
B Aa
C aa
D bb
(ABCD)
)
if answer == A
    good += 1
else
    bad.append(current)


current = 6
answer = input(
6. Wat is een allel
A Een soort cel
B Een variant van een gen
C Een chromosoom
D Een eiwit
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 7
answer = input(
7. Welk allel komt tot uiting als het dominant is
A Het recessieve allel
B Geen allel
C Het dominante allel
D Beide altijd
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


current = 8
answer = input(
8. Als iemand genotype Aa heeft en A is dominant, welk fenotype zie je
A Dominante eigenschap
B Recessieve eigenschap
C Geen eigenschap
D Beide
(ABCD)
)
if answer == A
    good += 1
else
    bad.append(current)


current = 9
answer = input(
9. Wat betekent genotype
A Uiterlijk
B Allelencombinatie van een organisme
C Leeftijd
D Gewicht
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 10
answer = input(
10. Wat betekent fenotype
A Het genotype
B De allelen
C Het waarneembare kenmerk
D De chromosomen
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


current = 11
answer = input(
11. Bij kruising Aa x Aa, hoeveel kans is er op aa
A 25%
B 50%
C 75%
D 100%
(ABCD)
)
if answer == A
    good += 1
else
    bad.append(current)


current = 12
answer = input(
12. Hoeveel mogelijke genotypen krijg je bij Aa x Aa
A 2
B 3
C 4
D 5
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 13
answer = input(
13. Welke combinatie van allelen is heterozygoot
A AA
B aa
C Aa
D BB
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


current = 14
answer = input(
14. Wat laat een stamboom zien
A DNA structuur
B Overerving in een familie
C Alleen genen
D Alleen ouders
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 15
answer = input(
15. In een stamboom is een vierkant meestal
A Vrouw
B Man
C Kind
D Ouders
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 16
answer = input(
16. In een stamboom is een cirkel meestal
A Man
B Vrouw
C Gen
D Allel
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 17
answer = input(
17. Wat betekent recessief
A Komt altijd tot uiting
B Alleen zichtbaar bij twee recessieve allelen
C Altijd dominant
D Alleen bij mannen
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 18
answer = input(
18. Hoeveel allelen heeft een mens meestal per gen
A 1
B 2
C 3
D 4
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 19
answer = input(
19. Bij genotype aa is het kenmerk
A Dominant
B Recessief
C Heterozygoot
D Onbekend
(ABCD)
)
if answer == B
    good += 1
else
    bad.append(current)


current = 20
answer = input(
20. Als A dominant is over a, welk genotype laat het dominante fenotype zien
A AA
B Aa
C AA en Aa
D aa
(ABCD)
)
if answer == C
    good += 1
else
    bad.append(current)


total = (good  20)  100
print(fYou scored {total}%.)

if bad
    print(Wrong questions, bad)
else
    print(All answers correct!)