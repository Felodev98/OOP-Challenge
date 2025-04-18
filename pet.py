class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Yum!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Zzz...")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing. Whee!")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print("-------------------------\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"\n--- {self.name}'s Tricks ---")
            for trick in self.tricks:
                print(f"- {trick}")
            print("-----------------------\n")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

# Example usage:
my_pet = Pet("Buddy")
my_pet.get_status()

my_pet.eat()
my_pet.play()
my_pet.get_status()

my_pet.sleep()
my_pet.get_status()

my_pet.train("Sit")
my_pet.train("Fetch")
my_pet.show_tricks()
my_pet.get_status()