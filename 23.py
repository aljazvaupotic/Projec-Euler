def divisors (num):
    vsota = 0
    for i in range(1,num):
        if(num%i == 0):
            vsota += i
    return vsota

limit = 28123
start = 25
numbers = [0]*28123
for i in range(28123):
    numbers[i]= i

abundandNumbers = []
for i in range(28123):
    x = divisors(i)
    if(x > i and x < 28123):
        abundandNumbers.append(i)
        print(i)
        print()

abundandNumbers.sort()
#print(abundandNumbers)

print(len(abundandNumbers))
for number1 in abundandNumbers:
    for number2 in abundandNumbers:
        y = number1+number2
        print(y)
        if y >= 28123:
            continue    
        numbers[y] = 0

print(sum(numbers))