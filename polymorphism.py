class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())


animals = [Bird(), Dog(), Cat()]
for animal in animals:
    animal_sound(animal)
