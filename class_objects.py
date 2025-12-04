###Task1###

# class Person:
    
#     def __init__(self,name,age,favorite)->None:
#         self.name=name
#         self.age=age
#         self.favorite=favorite

#     def greet(self):
#        print(f"Hello {self.name}! I`m {self.age}.")
    
#     def fav_age(self)->int:
#         return str(self.age+self.favorite)

# name_obj=Person(name="Anna",age=10,favorite=20)
# name_obj.greet()
# name_obj.fav_age()

# name_obj1=Person(name="Sasha",age=15,favorite=5)
# hu = name_obj1.fav_age()

###Task2###
# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*self.height

# square=Rectangle(2,9)
# print(square.area())

###Task3###
# class BankAccount:

#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance

#     def deposit(self,cash):
#         self.balance+=cash
    
#     def withdraw(self,withdraw):
#         self.balance-=withdraw
    
#     def display(self):
#         print(f"Balance {self.balance}")

# user1=BankAccount(account_number=1,balance=100)
# user1.deposit(10)
# user1.display()
# user1.withdraw(50)
# user1.balance=200
# user1.display()

###Task4###
# class Student:
#     def __init__(self,name,grades):
#         self.name=name
#         self.grades=list(grades)
    
#     def average_grade(self):
#         avr=sum(self.grades)/len(self.grades)
#         print(f"avr= {avr}")
#         return avr

# student1=Student(name="Sasha",grades=(10,12,9))
# student1.average_grade()


# ######
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
# def average_grade(self):
#         return sum(self.grades) / len(self.grades)
# # Створення об'єкта класу Student та виклик методу average_grade
# student = Student("Bob", [90, 85, 88, 92])
# print(f"{student.name}'s average grade is {student.average_grade()}")

###Task5###
# class Library:
#     def __init__(self,name):
#         self.name=name
#         self.books=[]
    
#     def add_book(self,add):
#         self.books.append(add)
    
#     def add_book(self,sub):
#         self.books.remove(sub)

#     def display(self):
#         print(f"number_books= {self.books}")

# name1=Library("Sasha")
# name1.add_book("Hero")
# name1.display()

