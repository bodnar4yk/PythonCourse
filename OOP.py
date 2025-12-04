###Task1###
class Shape:
    def __init__(self, color)->None:
        self.color=color
        
class Rectangle(Shape):
    def __init__(self,color,width, high)->None:
        super().__init__(color)
        self.width=width
        self.high=high

    def area(self):
        return self.width*self.high
    
# rect1=Rectangle(None,3,4)
# print(rect1.area())
class BankAccount:
    def __init__(self, balance):
        self.__balance=balance

    def __display(self):
        print(self.__balance)

    def deposit(self,a):
        self.__balance+=a
        self.__display()
    
    def withdraw(self,b):
        self.__balance-=b
        self.__display()

# acc1=BankAccount(1000)

# acc1.deposit(5)
# acc1.withdraw(10)
# acc1.deposit(50)
# acc1.withdraw(100)

# acc1.__balance = 100000000
# print(acc1.__balance)
# print(acc1._BankAccount__balance)

# acc1.deposit(5)

###Task3###
class Animal:
    def __init__(self):
        pass

    def speak(self):
        print(f"sillent")

class Dog(Animal):
    def speak(self):
        print("HAV")

class Cat (Animal):
    def speak(self):
        print("Meow")

class Fish (Animal):
    pass

# cat1=Cat()
# dog1=Dog()
# fish1=Fish()

# def voice(a):
#     a.speak()

# for i in [cat1,dog1,fish1]:
#     voice(i)


# voice(cat1)
# voice(dog1)
# voice(fish1)
# print(f"voice{cat1}")

###Task4###
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
class SalaryCalculator:
    def calculate_salary(self, employee):
        if employee.position == "Developer":
            return 80000
        elif employee.position == "Manager":
            return 100000
        else:
            return 50000
employee = Employee("John Doe", "Developer")
salary_calculator = SalaryCalculator()
print(f"Salary of {employee.name} is {salary_calculator.calculate_salary(employee)}")
        