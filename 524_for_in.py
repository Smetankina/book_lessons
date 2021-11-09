"""Давайте и мы напишем подобную программу. На вход ей будет поступать фраза и затем количество раз, которое эту фразу нужно повторить."""

phrase = input('Type the phrase, which we will repeat')
number_repetitions = int(input('Type number'))
for a in range(number_repetitions):
    print(phrase)
    a += a
