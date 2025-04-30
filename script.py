from random import randint
from random import choice
from random import shuffle


# составление случайного задания №4 с ЕГЭ
def examProblem(words):
    vowels = 'уеыаоэяиюё'
    chosenWords = []    # список с выбранными словами, слова в нём имеют ПРАВИЛЬНОЕ ударение
    modifiedWords = [0] * 5  # список со словами, выводимый пользователю
    correctAnswersCount = randint(2, 4)  # показывает, сколько ответов нужно оставить верными

    for i in range(5):
        wordIndex = randint(0,len(words) - 1)    # случайно выбранное слово
        chosenWords.append(words.pop(wordIndex))

    validIndeces = [0, 1, 2, 3, 4]      # индексы неиспользованных слов
    # добавление верных слов
    while len(modifiedWords) - modifiedWords.count(0) != correctAnswersCount:
        a = choice(validIndeces)
        validIndeces.remove(a)
        modifiedWords[a] = chosenWords[a]

    # изменение ударений в словах
    for i in validIndeces:
        inclVowels = []
        for j in range(len(chosenWords[i])):
            if chosenWords[i][j] in vowels:
                inclVowels.append(j)
        chosenVowel = choice(inclVowels)
        modifiedWords[i] = (chosenWords[i][:chosenVowel].lower() + chosenWords[i][chosenVowel].upper()
                            + chosenWords[i][chosenVowel + 1:].lower())

    wordPos = [0, 1, 2, 3, 4]   # индексы списка равны индексам слов в варианте
    shuffle(wordPos)
    print('Укажите варианты ответов, в которых ВЕРНО выделена буква, обозначающая ударный гласный звук. '
          'Запишите номера ответов.')
    for i in range(5):
        print(str(i + 1) + ': ' + modifiedWords[wordPos[i]])

    answer = input()

    wrongWords = []
    skippedWords = []
    for i in range(len(wordPos)):
        # проверка на неправильные ответы
        if modifiedWords[wordPos[i]] != chosenWords[wordPos[i]] and str(i + 1) in answer:
            wrongWords.append(chosenWords[wordPos[i]] + ' - ' + modifiedWords[wordPos[i]])
        # проверка на пропущенные ответы
        if modifiedWords[wordPos[i]] == chosenWords[wordPos[i]] and str(i + 1) not in answer:
            skippedWords.append(chosenWords[wordPos[i]])



    if len(wrongWords) == 0 and len(skippedWords) == 0:
        print('Верно!')
    else:
        print('Неверно!')
        if len(wrongWords) > 0:
            print('Были допущены ошибки в следующих словах: (пары расположены следующим образом: верное слово - неверное слово)')
            print('\n'.join(wrongWords))
        if len(skippedWords) > 0:
            print('Были пропущены следующие слова:')
            print('\n'.join(skippedWords))

    return 1

with open('dictionary.txt', encoding='UTF-8') as file:
    s = [x.strip() for x in file.readlines()]

nouns = s[s.index('--Существительные--') + 1:s.index('--Прилагательные--')]
adjectives = s[s.index('--Прилагательные--') + 1:s.index('--Глаголы--')]
verbs = s[s.index('--Глаголы--') + 1:s.index('--Причастия и деепричастия--')]
participles = s[s.index('--Причастия и деепричастия--') + 1:s.index('--Наречия--')]
adverbs = s[s.index('--Наречия--') + 1:]

print('Welcome to the gym, buddy :p')
while True:
    print('\n')
    print('1. Составить случайное задание формата ЕГЭ')
    print('0. Выход')
    userChoice = input()

    if userChoice == '1':
        examProblem(nouns + adjectives + verbs + participles + adverbs)
    if userChoice == '0':
        exit('SEX')
