# # product = input("Введи назву товару: ")
# # price = float(input("Ціна за одиницю: "))
# # quantity = int(input("Кількість: "))
# # delivery = input("Потрібна доставка? (так/ні): ")

# # total = price * quantity

# # if delivery == "так":
# #     total += 40 # додаємо 40 грн за доставку

# # print("Разом до сплати:", total, "грн")



# name = input("Ведіть своє ім'я: ")
# name = name.capitalize()
# age = int(input("Введіть свій вік: "))
# ticket = input("Чи ви маєте студентський квиток? (так/ні): ")

# age += 5 

# if age < 18:
#     category = "неповнолітній"
# elif age >= 18 and age <= 25:
#     category = "молодь"
# else:
#     category = "доослий"

# if ticket. lower() == "так":
#     discount_massage = "Ти отримуєш знижку на квиток" 

# else:
#     discount_massage = "Знижку не надано"

# print(f"Привіт, {name}!")
# print(f"Через 5 років тобі буде {age}.")
# print(f"Ти належиш до категорії {category}")
# print(discount_massage)



name = input("Ввудіть своє ім'я: ")
name = name.capitalize()
age = int(input("Введіть свій вік: "))
rating = int(input("Ваша оцінка: "))

if rating < 60:
    result = "Тест не складено"
elif 60 <= rating <= 89:
    result = "Тест складено"
else:
    result = "Тест складено відмінно!"

if age < 12:
    school = "Молодша школа"
elif 12 <= age <= 16:
    school = "Середня школа"
elif 16 < age <= 18:
    school = "Старша школа"
else:
    school = "Ви вже не навчаєтесь у школі"

print(f"Привіт, {name}!")
print(f"Ти навчаєшся в: {school}")
print(f"Твій результат: {result}")


# name = input("Введіть своє ім'я!: ")
# name = name.capitalize()
# age = int(input("Введіть свій вік:"))
# film = input("Введіть назву фільму: ")
# popcorn = input("Бажаєте попкрон? (так/ні): ")

# if age <=12:
#     price = 40

# elif 13 <= age <= 17:
#     price = 60

# else:
#     price = 80

# total = price

# if popcorn. lower() == "так":
#     total += 30

# print(f"Привіт, {name}!")
# print(f"Фільм: {film}")
# print(f"Сума до оплати: {total} грн")



# user_data = int(input("Введіть число: "))

# isHappy = True


# if isHappy or user_data == 6:
#     print("User is happy")

# elif user_data == 5:
#     print("Number is 5")

# else:
#     print("User is unhappy")


# if user_data != 5:
#     print("Ви увійшли")
#     if user_data > 6:
#         print("Number is bigger then 5")



# data = input()

# number = 5 if data == "Five" else 0

# # if data == "Five":
# #     number = 5
# # else:
# #     number = 0

# print(number)
