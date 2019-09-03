class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark!")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoing")


dog = Dog()
dog.walk()

cat = Cat()
cat.be_annoying()
