class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print('I am {} and I am {} years old'.format(self.name, self.age))

  def speak(self):
    print("I dont know what to say")

# Cat class (child class/ derived class) inherits methods of Pet class
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)  # call what is in the parent class / instantiate it
    self.color = color

  def show(self):
    print('I am {} and I am {} years old and I am {}'.format(self.name, self.age, self.color))

  def speak(self):
    print("Meow")

# Dog class inherits methods of Pet class
class Dog(Pet):
  def speak(self):
    print("Bark")

class Fish(Pet):
  pass


p = Pet("Puppy", 3)
p.show()

c = Cat("Tiger", 12, "Brown")
c.show()
c.speak()

d = Dog("Rocky", 5)
d.show()
d.speak()

f = Fish("Bubbles", 2)
f.speak() # I dont know what to say
