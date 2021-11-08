import inflect

sum = 0
p = inflect.engine()
for n in range(1,1000):
    word =(p.number_to_words(n))
    word = word.replace(",","")
    word = word.replace(" ","")
    word = word.replace("-","")
    print(word, "dolzina je",len(word))
    sum += len(word)

print(sum+11)
