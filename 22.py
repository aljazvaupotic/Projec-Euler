
f = open("p022_names.txt","r")
data = f.read()
data = data.replace('"','')
names = data.split(",")
print(names)
names.sort()
print(names)

valueOfLetter = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F"	: 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P"	: 16,
    "Q"	: 17,
    "R" : 18,
    "S" : 19,
    "T"	: 20,
    "U"	: 21,
    "V"	: 22,
    "W"	: 23,
    "X"	: 24,
    "Y" : 25,
    "Z" : 26
}
pos = 1
nameScore = [0]*len(names)
for name in names :
    current = 0
    for char in name:
        current += valueOfLetter.get(char)
    nameScore[pos-1] = current * pos
    pos += 1
    

print(sum(nameScore))