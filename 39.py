""" If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised? """

import math
def generate(num):
    out = 0
    for a in range(1,num-2):
        for b in range(a, num-a):
            if(a+b > num):
                break
            c = math.sqrt(a**2 + b**2)
            if (c % 1 == 0):
                if a+b+c == num:
                    out += 1

    #print(out)                
    return out    
m = []

print(generate(840))

#for i in range (1, 1001):
#   m.append(generate(i))
print(m)
print(max(m))
print(m.index(max(m))-1)

