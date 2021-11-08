# double base palindrom

def toBinary(number):
    if number == 0: 
        return 0
    else: 
        return (number % 2 + 10 * 
                toBinary(int(number / 2)))

def isPalindrom(number):
    numberRightway = str(number)
    numberReverse = numberRightway[::-1]
    return numberRightway == numberReverse


MAX = 10 ** 6
add = 0

for i in range(1,MAX+1):
    if isPalindrom(i):
        print(i, "je palindrom")
        x = toBinary(i)
        if(isPalindrom(x)):
            add += i

print(add)