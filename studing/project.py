# amount = int(input('Скільки чисел ви хочете ввести?: '))
# nums = []
# for i in range(amount):
#     number = int(input(f'Введіть число {i + 1}: '))
#     nums.append(number)
# nums = tuple(nums)

# even_count = 0
# for num in nums:
#     if num % 2 == 0:
#         even_count += 1

# print(f'Ваші числа: {nums}')
# print(f'Сума парних чисел: {even_count}')
# print(f'Сума: {sum(nums)}')
# print(f'Максимаьне число: {max(nums)}')

# amount = int(input('Скільки продуктів ви хочете ввести?: '))
# products = []
# for i in range(amount):
#     number = input(f'Введіть перший продукт: {i + 1}: ')
#     products.append(number)
# products = tuple(products)


# count = 0
# for el in products:
#     if len(el) > 5:
#         count += 1

# print('Ващ список продуктів: ', products)    
# print('Продуктів у назві яких більше 5 символів: ', count)


# amount = int(input('Скільки чисел ви хочете ввести?: '))
# numbers = []
# for i in range(amount):
#     chislo = int(input(f"Введіть число: {i + 1} "))
#     numbers.append(chislo)
# corteje = tuple(numbers)

# count = 0
# for el in corteje:
#     if el % 2 == 0:
#         count += 1

# print(f'Сума ваших чисел: {sum(corteje)} ')
# print(f'Парних чисел: {count}')
# print(f'Найбільше число: {max(corteje)}')
# print(f'Найменше число: {min(corteje)}')

spend = int(input('Скільки витрат ви хочете ввести?: '))
expenses = []
for i in range(spend):
    nums = float(input(f'Введіть суму втрати: {i+1} '))
    category = input(f'Введіть категорію для витрати: (їжа або транспорт) {i+1} ')
    expenses.append((nums, category))
transport_total = 0
food_total = 0
count = 0
all_sums = []
corteje = tuple(expenses)

for nums, category in expenses:
    all_sums.append(nums)
    if category == 'їжа':
        food_total += nums
    else:
        transport_total += nums
    if nums > 100:
        count += 1



print(f'Сума витрат: {sum(all_sums)} ')
print(f'Найбільша витрата: {max(all_sums)} ')
print(f'Найменша витрата: {min(all_sums)} ')
print(f'Витрат більше 100 грн: {count}')
