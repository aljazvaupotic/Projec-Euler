""" An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 """


w = ""

i = 1

while len(w) < 1000001:
    w += str(i)
    #print(len(w))
    i+= 1
a = 1
pow = 0
while pow <= 6:
    #print(pow, 10**pow, w[10**pow])
    a *= (int(w[10**pow - 1]))
    pow += 1

print(a)