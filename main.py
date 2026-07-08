# programming concepts

# operators in python: = - + / %
#variable in python 
a = 5 # integer
b = "leo" # string
c = 5.5 # float or decimal
d = [a,b, c, "kyr"]  # list
e = {"name":"kyr","age": a}# dictionary

f = True # bool
g = a > 7 # bool

h = a == 5 # bool
print(e["name"])
print(g)
print(e)
print(e["age"])
print(d)
print(h)

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age 
    
    def __str__(self):
        return f"name: {self.name}, Age: {self.age}"

    def fight(self):
        return f"{self.name} can fight"    



person = Human("kyrian",24)
print(person)
print(person.name)
print(person.fight())

class Female(Human):
    def cry(self):
        if self.age >= 30 and self.age <= 59:
            return f"my name is {self.name}.i cry even tho i am an old woman"
        elif self.age >= 50:
            return f"my name is {self.name}.i cry even tho my mates have grand children"
        return f"my name is {self.name}. I cry because i am a woman"
        
    def dance(self):
        dance_steps = [1, 2, 3, 4, 5]     
        dance = []
        for step in dance_steps:
            dance.append(f"dance step {step}")
        return dance

new_person = Female("Ada",41)        

print(new_person)
print(new_person.cry())
print(new_person.dance())
print(", ".join(new_person.dance()))
