"""
Все 4-буквенные слова, составленные из букв М, У, Х, А записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
 
1. АААА
2. АААМ
3. АААУ
4. АААХ
5. ААМА

Напишите номер слова ХУХХ
"""
LETTERS = 'А М У Х'.strip().split()
counter = 0


def gen_string(count, prefix):
    if count == 0:
        global counter
        counter += 1
        return print(counter, prefix)
    for i in range(4):
        gen_string(count - 1, prefix + LETTERS[i])

default_counter = 4
gen_string(default_counter, '')

