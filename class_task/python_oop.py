class Human:
    number_of_nose = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        return print(f"Hello {self.name} ")

    def walking(self):
        return print(f"{self.name} is walking")

    def __str__(self):
        return f"{self.name}"


plateau_man = Human("Retnaa")
plateau_man.greet()
plateau_man.walking()
print(plateau_man.name)
print(str(plateau_man))
