listStevilk = [0] * 10
summand = []
for a in range(1,1000):
    for b in range(100,10000):
        listStevilk = [0] * 10
        c = a*b
        alist = list(map(int,(str(a))))
        blist = list(map(int,(str(b))))
        clist = list(map(int,(str(c))))
        if 0 in alist or 0 in blist or 0 in clist:
            continue
        for num in alist :         
            listStevilk[num] += 1
        for num in blist :
            listStevilk[num] += 1
        for num in clist :
            listStevilk[num] += 1
        add = True
        for i in range(1,10):
            if(listStevilk[i] != 1):
                add = False
        if(add == True and c not in summand):
            summand.append(c)
print(summand)
print(sum(summand))