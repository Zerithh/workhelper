# word = "Footall, basketball, skate"
# # # # print(word.count("p"))
# # # # print(word.upper()) #переводить усе в верхній регістр
# # # print(word.lower()) #пееводить текст  нижній регістр
# # # # print(word.isupper()) #перевіряє чи рядок у верхньому регістрі та вертає значення True або False
# # # # print(word.islower()) #перевіряє чи рядок у нижньому регістрі та вертає значення True або False
# # # print(word.capitalize()) #переводить першу бувку в ерхній регістр
# # # print(word.find("pr")) #знайти індекс вказаної букви
# # # print(word.split(',')) #розділити рядок символом який вкажемо, та записати у список

# hobby = word.split(", ")

# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()

# result = ", ".join(hobby)
# print(result)

# word = "i, Love, Dana"
# hobby = word.split(', ')
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()

# result = ", ".join(hobby)
# print(result)


# word = 'anNa, petrO, ivAn'
# names = word.split(', ')
# for i in range(len(names)):
#     names[i] = names[i].capitalize()

# print(names)


# count = int(input("Введіть кількість продуктів: "))
# numbers = []
# for el in range(count):
#     product = input(f"Введи назву продукту {el + 1}: ")
#     product = product.capitalize()
#     numbers.append(product)
# result = ", ".join(numbers)
# print("Твій список покупок:", result)

# count = int(input("Введи кількість фільмів: "))
# list = []
# for el in range(count):
#     film = input(f"Введи назву фільму {el + 1}: ")
#     film = film.capitalize()
#     list.append(film)
# result = ",".join(list)
# print("Твій список фільмів: ", result)

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(data[1::2])
print(data[-1:-6:-1])