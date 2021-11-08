
distTerms =[]

for a in range(2,101):
    for b in range(2,101):
        num = a ** b
        if num not in distTerms:
            distTerms.append(num)
            distTerms.sort()

print(len(distTerms))