# country = {'code': 'UA', 'name': 'Ukraine', 'population': 45}
# # country = dict(code='UA', name='Ukraine')
# # print(country['name'])

# # for key, value in country.items(): # items - виводить не тільки ключ а й значення, але треба створити дві змінні
# #     print(key, ' - ', value)

# print(country.get('name')) # дозволяє вивести ключ без квадратних дужок (заміняє кв. дужки)
# country.clear() # очищує словник
# country.pop('name') # видаляє значення, звертаємось по ключу
# country.popitem() # видаляє останній елемент з словника

# print(country.keys()) # дозволяє вивсести тільки ключі
# print(country.values()) # дозволяє отримати тільки значення
# print(country.items()) # виводимо і ключі і значення, але кожен елемент це визначенний кортеж який складається з 2 елементів

# country['code'] = 'None' # замінюємо значення ключа


# name = input("Введіть своє імя: ")

# dana = {
#     'user1': {
#         'first_name': 'Daniella', 
#         'last_name': 'Lutsenko',
#         'age': 20,
#         'place_of_work': 'itravel',
#         'name_of_cat': ('Снєжа'),
            
#     }

# }
    

# if name == "Даніела":
#     print(dana['user1'])
# else:
#     print('йди звідси')

slovar = {'name': 'Vasya', 'surname': 'Petrov', 'counrty': 'Poland', 'telefon_number': '48452092061'}

for key, value in slovar.items():
    print(key,' - ', value)