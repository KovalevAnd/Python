# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('my_f_2.txt', 'r') as f:
    kol_str = 0
    kol_sl = 0
    for line in f:
        for el in line.split(' '):
            kol_sl = kol_sl + 1
        kol_str = kol_str + 1
        print('в строке №' + str(kol_str) + ' - ' + str(kol_sl) + ' слов(а)')
        kol_sl = 0
    print('в выбранном файле ' + str(kol_str) + ' строк(и)')
