class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

class DogSaver:
    def save_to_file(self, dog):
        with open("dog.txt", "w") as f:
            f.write(dog.name)
