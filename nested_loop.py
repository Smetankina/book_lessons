'сколько 6ти буквенных слов можно составить из слова ТЫКВА, начинающихся и заканчивающихся с согласных , содержащих 2 гласные'
cycle=0
for a1 in 'тыква':
    for a2 in 'тыква':
        for a3 in 'тыква':
            for a4 in 'тыква':
                for a5 in 'тыква':
                    for a6 in 'тыква':
                        word = a1+a2+a3+a4+a5+a6
                        if word[0] in 'ткв' and word[-1] in 'ткв':
                            if word.count('ы')+word.count('а')==2:
                                cycle+=1
print(cycle)