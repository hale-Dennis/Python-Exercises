

class Animal:

    #class variable 
    type = "mammal"

    def __init__(self, habita):
        self.habitat = habita

    def sound(self):
        print("Some sound")
    
    def get_habitat(self):
        print(self.habitat)


class Dog(Animal):

    def __init__(self, habitat):
        super().__init__(habitat)
    
    def sound(self):
        print("woof woof")


scooby = Dog("house")
scooby.get_habitat()
scooby.sound()
