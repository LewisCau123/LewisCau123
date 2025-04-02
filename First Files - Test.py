'''
print("Hello World")

name = input("Hello, What is your name?")

if name == "Lewis":
    print(f"Hello {name}")
else:
    print("Hello Stranger")



def multiple_print(string, n):
    print(string * n)
    print()

multiple_print("Hello", 5)



def convert(t):
    return t*9/5+32
print(convert(20))


#Write a function to take name of the student as input and print wish message by name.

def studentname(name):
    input("What is your name?")
    print(f"Hello {name}")


studentname("Lewis")
'''

class MyClass:
    x = 50


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Shahana", 36)
print(p1.name)
print(p1.age)