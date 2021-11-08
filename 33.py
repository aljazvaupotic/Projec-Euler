import math

#def lcm(a, b):
#   return abs(a*b) / math.gcd(a, b)
test = []
stevilke = []
for a in range (10,100):
    for b in range(a+1,100):
        alist = list(map(int,(str(a))))
        blist = list(map(int,(str(b))))
        for m in range(1,10):
            if m in alist and m in blist:
                num = a/b

                alist.remove(m)
                blist.remove(m)
                upper = sum(alist)
                denom = sum(blist)
                c = 0
                if(upper > 0 and denom > upper):
                    c = upper/denom
                    #print(c, "primerjam z okrajsanim", num)
                if num == c:
                    stevilke.append(num)
                    #print(upper,denom)
                    test.append(denom/upper)
                        
print(stevilke)
result  = 1
result1 = 1
for x in stevilke:
    result *= x
for x in test:
    result1 *= x

print(round(1/result))
print(result1)