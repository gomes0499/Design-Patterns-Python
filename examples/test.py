from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Lion(Animal):
    def speak(self):
        return "Roar"

class Tiger(Animal):
    def speak(self):
        return "Growl"

class Bear(Animal):
    def speak(self):
        return "Grr"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Lion":
            return Lion()
        elif animal_type == "Tiger":
            return Tiger()
        elif animal_type == "Bear":
            return Bear()
        else:
            raise ValueError("Invalid animal type")

factory = AnimalFactory()

# Criar um leão e fazê-lo falar
animal1 = factory.create_animal("Lion")
print(animal1.speak())  # Output: Roar

# Criar um tigre e fazê-lo falar
animal2 = factory.create_animal("Tiger")
print(animal2.speak())  # Output: Growl

# Criar um urso e fazê-lo falar
animal3 = factory.create_animal("Bear")
print(animal3.speak())  # Output: Grr
