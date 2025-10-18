# nums = (3, 6, 9, 12, 15)
# number = int(input('Введіть число: '))
# calculate = nums.count(number)
# if calculate > 0:
#     print('Є в списку')
# else:
#     print('Немає в списку')


# nums = (3, 6, 9, 12, 15)
# number = int(input('Введіть число: '))

# print('Числа, які не дорівнюють введеному:')

# for el in nums:
#     if el != number:
#         print(el)



count = int(input('Скільки чисел ви хочете ввести?: '))
numbers = []

for i in range(count):
    num = int(input(f'Введіть число: {i + 1}:' ))
    numbers.append(num)
numbers_tuple = tuple(numbers)
even_count = 0
for num in numbers_tuple:
    if num % 2 == 0:
        even_count += 1

print('Кількість парних чисел у вашму списку: ', even_count)