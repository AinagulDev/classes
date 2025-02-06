class Animal:
    name="None"
    age=1

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

    def run(self):
        print("Running...")

obj_1=Animal()

print(obj_1.name)
print(obj_1.age)
eat()
sleep()
run()

class Person:
    def  __init__(self,name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

    def info(self):
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Age: {self.age}')
        print('#' * 20)

person_1=Person ("Arsen","Kenjegulov",22)
person_2=Person("Nurbol","Kadyrbekov",17)
person_3 = Person("Emir", "Kachkynov", 13)
person_4 = Person("Asylbek", "Arstanbekov", 14)
person_5 = Person("Ainagul", "Azhybaeva", 38)
person_6 = Person("Elnara", "Kasymbekova", 15)
person_7 = Person("mirzhana", "Begalieva", 15)

users = [person_1,person_2,person_3,person_4,person_5,person_6,person_7]

for user in users:
    if user.name[0] == "A":
        user.info()





