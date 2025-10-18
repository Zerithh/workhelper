# # # nums = [5, 7, 2, 4, 7, True, "Hello", 6.7, [5, 7]]

# # # nums[0] = 50
# # # nums[5] = 1.01

# # # print(nums[-1][1])


# # numbers = [5, 2, 7]
# # # numbers[3] = 100
# # numbers.append(100) #додаємо до кінця списку значення
# # numbers.insert(1, True) #додаємо значення True на місце 2. Один елемент
# # b = [5, 6, 8]
# # numbers.extend(b) #додаємо декілька значень, ще один список
# # numbers.sort() #сортування елементів
# # # numbers.reverse() #зміна порядку чисел
# # numbers.pop(-2) # останній елемент видаляється (або вказати індекс)
# # numbers.remove(6) #видаляє елемент який ми вкажемо 

# # # numbers.clear() #видаляє абсолютно усе
# # print(len(numbers)) #порахує довжину вказанного списку

# # # print(numbers.count(True)) #рахує кількість елементів які співпадають з вказаним значенням



# nums = [5, 2, 7, "50", False]

# for el in nums:
#     el *= 2
#     print(el)


# n = int(input("Enter lenght: "))

# user_list = []

# i = 0
# while i < n:
#     string = "Enter element number" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1

# print(user_list)


n = int(input("Скільки людей голосує?: "))

user_list = []

i = 0
while i < n:
    fruit = "Введіть свій улюбленний фрукт: " + str(i + 1) + ": "
    user_list.append(input(fruit))
    i += 1 

print("Всі голоси:", user_list)

