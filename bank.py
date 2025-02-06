'''class bank:
    def __init__(self,first_name,last_name,age,balance=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def info(self):
        print(f'Name: {self.first_name}')
        print(f'Surname: {self.last_name}')
        print(f'Age: {self.age}')
        print('#*20')

    def get_balance(self):
        print(f'{self.first_name} balance: {self.balance}')

bank_1 = Bank("Arsen", "Kenzhegulov", 22)
bank_2 = Bank("Nurbol", "Kadyrbekov", 17)
bank_3 = Bank("Emir", "Kachkynov", 13)
bank_4 = Bank("Asylbek", "Arstanbekov", 14)
bank_5 = Bank("Ainagul", "Azhybaeva", 38)
bank_6 = Bank("Elnara", "Kasymbekova", 15)
bank_7 = Bank("mirzhana", "Begalieva", 15)'''



#Task-1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}')

# car_1=Car()
# car_1.display_info()
    

#Task-2
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if  amount > 0:
            self.balance+=amount
        print(f'Баланс пополнен на {amount}. Новый баланс:{self.balance}')


    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Недостаточно средств!")

#account = BankAccount("Алим", 500)
#account.deposit(200)
#account.withdraw(1000)

# Task-3
class Student:
    def __init__(self,name,age,grades):
       self.name=name
       self.age=age
       self.grades=grades

    def average_grade(self,name,age,grades):
        total_grades=0
        for i in grades:
            total_grades+=i
        return (f'Ortocho baa: {total_grades/4}')

student1=Student("Aijan",20,[90,85,88,92])
print(student1.average_grade("Aijan",20,[90,85,88,92]))


# Task-4
class Calculator:
    def __init__(self,add,subtract,multiply,divide):
        self.add=add
        self.subtract=subtract
        self.multiply=multiply
        self.divide=divide

