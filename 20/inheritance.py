class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def jump(self, h):
        print(self.name, "jump", h, "см")


class Cat(Animal):
    def meow(self):
        print("meow!")


class Dog(Animal):
    def ruff(self):
        print("ruff!")


c = Cat("cot", 10)
d = Dog("dag", 10)
c.jump(1)
d.jump(2)
c.meow()
d.ruff()
