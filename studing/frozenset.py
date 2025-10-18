# # data = set('hello')
# # print(data)

# # data = {3, 5, 7, 4, 1}
# # data.add(32) # додаємо значення до множества
# # data.update(['32', True, 4.6]) # додаємо декілька значень 
# # data.remove(True) # видаляємо елемент
# # data.pop() # видаляємо перший елемент
# # data.clear() # очищуємо множество

# nums = [3, 5, 6, 3, 4, 6]
# new_nums = set(nums) # перетворюємо список у множество

# print(new_nums)

# new_data = frozenset([3, 5, 2, True, 4.6, False, '32']) # кортеж + множество (не можна змінювати - множество з свойствами кортежа)

# names = int(input('Скільки іммен ви хочете ввести?: '))

# data = []

# for i in range(names):
#     num = input(f'Введіть імя: {i+1} ')
#     data.append(num)

# new_data = set(data)
# dlina = len(new_data)


# print('Список імен:', new_data)
# print('Унікальних імен:', dlina)

# names1 = int(input('Скільки імен ви хочете ввести в перший список?: '))
# spisok1 = []
# for i in range(names1):
#     num1 = input(f'Введіть імя: {i+1} ').strip()
#     spisok1.append(num1)
# data1 = set(spisok1)

# names2 = int(input('Скільки імен ви хочете ввести в другий список?: '))
# spisok2 = []
# for el in range(names2):
#     num2 = input(f'Введіть імя: {el+1} ').strip()
#     spisok2.append(num2)
# data2 = set(spisok2)

# my_set = data1 & data2

# print('Перший список:', data1)
# print('Другий список:', data2)
# print(f'Спільні імені у списках: {my_set}' )  


# tom = {
#     'gloves',
#     'knifes',
#     'helmet',
#     'water',
#     'money', 
#     'documents'
# }

# mike = {
#     'sports uniform',
#     'gloves',
#     'knifes',
#     'helmet',
#     'documents'
# }

# jef = {
#     'helmet',
#     'water',
#     'money', 
#     'documents',
#     'sraka',
#     'dupa',
# }


# things = tom.union(mike)
# shit = things.union(jef)
# print(shit)

number = 7

guess = int(input('Введіть число: '))

while guess != number:
    print('Спробуй ще раз!')
    guess = int(input('Введіть число: '))
print('Вгадав! Молодець!')