class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"I'm {self.name}")

    def scream(self):
        print(f"I'm {self.name} and I'm mad!")


person = Person("J.T.")
person.talk()
person.scream()
