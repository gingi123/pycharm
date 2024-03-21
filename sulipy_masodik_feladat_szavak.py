import random



words = ["fuvola","csirke","adatok","asztal","fogoly","bicska","farkas","almafa","babona","gerinc","dervis","bagoly","ecetes","angyal","boglya"]
random_word = random.choice(words)
print(F"{random_word=}")
x = 1
stop = False
input_words = input('Kérem a tippet: ')
while input_words != random_word:
    if input_words == 'stop':
        stop = True
        break
    print('Az eredmény: ',end='')
    for index in range(6):
        if input_words[index] == random_word[index]:
                print(input_words[index], end='')
        else:
            print('.',end='')
    input_words = input('\n\nKérem a tippet: ')
    x = x + 1
if not stop:
    print(f'{x} tippelessel sikerült kitalálni.')