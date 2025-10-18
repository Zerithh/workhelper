# data = input('Введіть текст: ')

# file = open('data/text.txt', 'a')

# file.write(data + '\n')

# file.close()


# file = open('data/text.txt', 'r')

# # print(file.read())

# for line in file:
#     print(line, end='')

# file.close()

# do = input('Що ти хочеш зробити?\n1 - додати запис\n2 - прочитати усі записи\nВаш вибір:')

# if do == '1':
#     file = open('data/text.txt', 'a')
#     sign = input('Введіть запис: ')
#     file.write(sign + '\n')
#     file.close()

# elif do == '2':
#     file = open('data/text.txt', 'r')
#     print(file.read())
#     file.close()
# else:
#     print('Вибір неправильний!')


# shoppng_list = []
# while True:
#     item = input('Введіть продукт (або "стоп" щоб завершити): ')
#     if item.lower() == 'стоп':
#         break
#     shoppng_list.append(item)

# note = input('Введи свою нотатку: ')

# with open('data/text.txt', 'a', encoding='utf-8') as f:
#     f.write(note + '\n')

# print('\nВсі нотатки: ')
# with open('data/text.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(' - ' + line.strip())

# name = input('Введіть назву файлу: ')

# try:
#     with open(name, 'r', encoding='utf-8') as f:
#         content = f.read()
#         print('Файл відкрито!')

#         copy_name = 'копія' + name

#         with open(copy_name, 'w', encoding='utf-8') as copy_file:
#             copy_file.write(content)
#         print(f'Файл скопійовано як {copy_name}')


# except FileNotFoundError:
#     print('Файл не знайдено!')


name = input('Введіть назву файлу: ')

try:
    with open(name, "r", encoding="utf-8") as f:
        content = f.read()
        print('Файл відкрито!')
except FileNotFoundError:
    print('Файл не знайдено')
    content = ''

lines = content.splitlines()
line_count = len(lines)

word_count = len(content.split())

count = len(content)

print('Кількість рядків у файлі: ', line_count)
print('Кількість слів у файлі: ', word_count)
print('Кількість симоволів у файлі: ', count)