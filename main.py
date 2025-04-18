from pet import Pet

if __name__ == "__main__":
    my_pet = Pet("Shadow")
    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    my_pet.train("Roll over")
    my_pet.train("Speak")
    my_pet.show_tricks()
    my_pet.get_status()
