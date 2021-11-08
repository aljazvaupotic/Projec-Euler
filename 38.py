""" Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1? """



def isPandi(num):
    p = [0,1,1,1,1,1,1,1,1,1]
    word = list(map(int,(str(num))))
    print(sum(p))
    if 0 in word:
        return False
    else:
        for stevka in word:
            if p[stevka] == 1:
                p[stevka] = 0
    print(sum(p),num)
    return (sum(p) == 0)

m = 0

for i in range(9999,0,-2):
    x = 1
    l = ""
    while(x < 10 and len(l) < 9):
        l += str(i*x)
        x+= 1
    if(len(l) == 9):
        if(isPandi(l) and int(l) > int(m)):
            m = l
            print(m)

print(m)