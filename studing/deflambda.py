# def greet_user(name):
#     if name == '':
#         print('Привіт друже')
#     else:
#         print('Привіт', name)

# num = input('Введіть своє імя: ')
# greet_user(num)

# def sum_numbers(a, b):
#     return a + b

# numbers1 = int(input('введіть число 1: '))
# numbers2 = int(input('введіть число 2: '))
# sum_numbers(numbers1, numbers2)
# print("Сума чисел:", sum_numbers(numbers1, numbers2))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#        return False

# chisla = int(input('Скільи чисел ви хочете ввести?: '))
# count = chisla
# numbers = []
# for i in range(count):
#     el = int(input('Введіть число: '))
#     numbers.append(el)

# even_cont = 0

# for me in numbers:
#     if is_even(me):
#         even_cont += 1
    
# print("Кількість парних чисел:", even_cont)

# def summa(a, b):
#     return a + b

# res = summa(5, 7)
# print(res)

# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#     print(min_number)

# nums1 = [5, 7, 2, 9, 4]
# minimal(nums1)

# nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
# minimal(nums2)

# num = int(input('Введіть число: '))

# def is_even(number):
#     return number % 2 == 0
# print(is_even(num))

# func = lambda x, y: x * y
# print(func(5, 2))

# def greet(name):
#     hej = (f'Привіт {name}! Гарного дня! ')
#     return hej 

# user_name = input('Введіть імя: ')
# message = greet(user_name)
# print(message)

# def repeat_phrase(phrase, time):
#     for i in range(time):
#          print(phrase)

# kik = input('Введіть фразу: ')
# pic = int(input('Скільки разів ви хочете ввести фразу?; '))
# repeat_phrase(kik, pic)


# total = 0 

# a = 1
# b = 2


# while b <= 4000000:
#     if b % 2 == 0:
#         total += b

#     next_fib = a + b
#     a = b
#     b = next_fib

# print(total)

# def prime_factors(n): # визначення простих множників числа
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i == 0:
#             factors.append(i)
#             n = n // i
#         else:
#             i += 1
#     if n > 1:
#         factors.append(n)
#     return factors

# print(prime_factors(600851475143))


# sum_of_square = 0

# for i in range(1, 100):
#     sum_of_square += i * i
# print(sum_of_square)

# sum_of_square = sum(i*i for i in range(1, 101)) # сума квадратів та квадрат суми

# square_of_sum = 0

# for el in range(1, 101):
#     square_of_sum += el
#     square = square_of_sum * square_of_sum

# difference = square - sum_of_square
# print(difference)





# def is_divisible(n): # знаходження найменшого числа, на яке діляться усі числа від 1 до 20 включно
#     for i in range(1, 21):
#         if n % i != 0:
#             return False
#     return True

# n = 1
# while True:
#     if is_divisible(n):
#         break
#     n += 1

# print("Найменше число:", n)



