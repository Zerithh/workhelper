# for i in range (1, 6, 2): # 1 = початкове значення, 6 кінцеве значення, 2 = крок з яким буде збільшуватись значення
    # print(i)

# secret_number = 7

# while True:
#     user_input = input("Вгадай число або введи 'вихід': ")

#     if (user_input) == "вихід":
#         print("Програму завершено!")
#         break
 
#     guess = int(user_input)

#     if guess == secret_number:
#         print("Ти вгадав число")
#         break
#     else: 
#         print("Не вгадав, спробуй ще раз")

# right_password = "qwerty123"

# while True:
#     user = input("Введи пароль: ")

#     if user == "вихід":
#         print("До зустрічі!")
#         break

#     if user == right_password:
#         print("Доступ надано!") 
#         break
#     else:
#         print("Не правиельний пароль. Спробуй ще раз")


digit = 15

while True:
    user = input("Введіть число: ")

    if user == "вихід":
        print("Допобчаення")
        break

    ex = int(user)

    if user == digit:
        print("Ви вгадали, вітаю!")
        break
    

    if user >= 15:
        print("Загадане число менше")
    else: 
        print("Загадане число більше")
