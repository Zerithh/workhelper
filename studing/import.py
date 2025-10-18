# import math_operations as mo
# from string_utils import greet 

# print(greet('Mykhailo'))
# print('2+3=', mo.add(2,3))
# print('4*5=', mo.multiply(4, 5))
# print('Square of 7 =', mo.square(7))

# class Cat: 
#     name = None
#     age = None
#     IsHappy = None

#     def __init__(self, name, age, IsHappy):
#         self.set_data(name, age, IsHappy)
#         self.get_data()

#     def set_data(self, name, age, IsHappy):
#         self.name = name
#         self.age = age
#         self.IsHappy = IsHappy

#     def get_data(self):
#         print(self.name, 'age:', self.age, '. Happy:', self.IsHappy)


# cat1 = Cat('Barsik', 3, True)

# cat2 = Cat('Снєжа', 2, False)



# class Building:
#     year = None
#     city = None

#     def __init__(self, year, city):
#         self.year = year
#         self.city = city 

#     def get_info(self):
#         print('Year', self.year, '. City', self.city)

# class School(Building):
#     pupils = 0


# import webbrowser


# def validator(func):
#     def wrapper(url):
#         if '.' in url:
#             func(url)
#         else:
#             print('Невірний URL')
#     return wrapper


# @validator
# def open_url(url):
#     webbrowser.open(url)

# open_url('https:/itproger.com')

