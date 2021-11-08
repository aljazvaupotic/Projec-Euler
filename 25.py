
y = 1
x = 1
m = 2
while (len(str(x)) < 1000):
    new = y+x
    y = x
    x = new
    m += 1

print(m,y,x)