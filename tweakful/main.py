# number = [1,2,3,4,5, 6, 7, 8]

# def filter(number):
#     filt_num = [n for n in number if n % 2 == 0]
#     return filt_num
    
# result = filter(number)
# print(result)

    
# students = [
#     {"name": "Anna", "score": 90},
#     {"name": "Asan", "score": 60},
# ]

# def top_students(students, num):
#     listest = []
#     for student in students:
#         if student["score"] >= num:
#             listest.append(student["name"])
#     return listest        
        
# stud = top_students(students, 70)
# print(stud)


# messages = [
#     "WARNING: url is not found",
#     "hello world",
#     "URGENT: server is down",
# ]

# def alert(messages):
#     all = []
#     for world in messages:
#         if "WARNING" in world or "URGENT" in world:
#             all.append(world)
#     return all
    
# al = alert(messages)
# print(al)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# def count_num(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count += 1
#     return count

# num = count_num(numbers)
# print(num)



# string = " Python is AWESOME"

# def normalize(string):
#     str1 = string.strip(" ").lower()
#     print(str1)

# normalize(string)


# number = [10, 10, 10, 10, 10]

# def sum_numbers(num):
#     total = 0
#     for i in num:
#         total += i
#     return total

# nums = sum_numbers(number)
# print(nums)


# password = "abc123"

# def password_length(password):
#     return len(password) >= 6
        
# pas = password_length(password)
# print(pas)

# numbers = [1,2,3,4,10]

# def max(num):
#     start = num[0]
#     for i in num:
#         if i > start:
#             start = i
#     return start

# m = max(numbers)
# print(m)


# text = "python is very cool and so interesting"

# def count_text(text):
#     return len(text.split())

# c = count_text(text)
# print(c)


# words = ["cat", "elephant", "dog", "tiger"]

# def count_words(words):
#     new = []
#     length = [i for i in words if len(i) > 3]
#     new.append(length)
#     return new

# k = count_words(words)
# print(k)

# def count_words(words):
#     return [i for i in words if len(i) > 3]

# k = count_words(words)
# print(k)


# numbers = [1, 2, 3, 4, 5, 6]

# def odd_nums(num):
#     return [i for i in num if i % 2]

# n = odd_nums(numbers)
# print(n)


# grades = {"Math": 80, "English": 90, "Physics": 70}

# def sums(grades):
#     total = 0
#     for grade in grades.values():
#         total += grade
#     return total
        
    
# d = sums(grades)
# print(d)


# text = "The server is down"

# def contains_world(text, world):
#     for i in text:
#         if world in text:
#             return True
#         else:
#             return False

# def contains_world(text, world):
#     return world in text

# text = contains_world(text, "server")
# print(text)


# numbers = [1, 2, 3, 2, 4, 1, 5]

# def uniqe(num):
#     new = []
#     for i in num:
#         if i not in new:
#             new.append(i)
#     return new

# def uniqe(num):
#     return list(set(num))

# n = uniqe(numbers)
# print(n)


# def merge(d1, d2):
#     result = d1.copy()
#     result.update(d2)
#     return result

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}

# print(merge(dict1, dict2))

# numbers = [1, 2, 3, 4, 5, 6]

# def sum(num):
#     total = 0
#     for i in num:
#         if i % 2 == 0:
#             total += i
#     return total

# n = sum(numbers)
# print(n)




# number1 = int(input("Введите первое число:"))
# number2 = int(input("Введите второе число:"))
# operator = input("Выберите один из операторов '+-*/%' ")

# if operator == "+":
#     print(number1+number2)
# if operator == "-":
#     print(number1-number2)
# if operator == "*":
#     print(number1*number2)
# if operator == "/":
#     print(number1/number2)
    

    
    
    
# a = "Hello"
# b = "World"

# print()

# a = 10

# print(a)

# p = 100

# for i in range(p+1):
#     if i % 2 == 0:
#         print(i)




# int - тип данных число
# str - это строка
# list = списки
# turple - кортеж ()
# dict - словарь, хрнаит данные в виде ключ и значения
# set - множества
# def - функция
# bool - логический тип данных
# float - число с плавающий запятой

# number = 100

# for i in range(50, number+1):  
#     print(i)



# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# operator = input("Выберите тип действия '+-*/%' ")

# if operator == "+":
#     print(number1+number2)
# if operator == "-":
#     print(number1-number2)
# if operator == "*":
#     print(number1*number2)
# if operator == "/":
#     print(number1//number2)
# if operator == "%":
#     print(number1%number2)
    
    

# a = 20

# for i in range(a):
#     if i % 2 == 0:
#         print(i)
    
    

# def validate_username(username):
#     message = ""
    
#     if username[0].isdigit():
#         message += "Не должно начинаться с цифры" + "\n"
    
#     if 3 <= len(username) <= 15:
#         message += "Длина подходит" + "\n"
#     else:
#         message += "Не подходит длина" + "\n"
#     if username.isalpha():
#         message += "Не подходит, должна содержать число" + "\n"
#     if username.isdigit():
#         message += "Не подходит, должна содержать букву" + "\n"
    
#     print(message)
        
    

# validate_username("fvgjggfh7")
        
        
        



# my_string = "Hello"

a = 10
b = 30
c = 2
