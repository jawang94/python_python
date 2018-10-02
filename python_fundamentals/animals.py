class Animal:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print(self.health)
        return self

human = Animal("Jason",100)
human.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Golden Retriever")
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print(f"I am a dragon and my health is {self.health}")
        return self

dragon1 = Dragon("Svardold")
dragon1.walk().walk().walk().run().run().fly().displayHealth()