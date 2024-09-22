class Animal:
    def __init__(self, region, animal_type, color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal

    def animal_bio(self):
        print(f"\tAnimal Passport:")
        print(f"\tFound in: {self.region}")
        print(f"\tSpecies: {self.animal_type}")
        print(f"\tColor: {self.color}")
        print(f"\tDangerous: {self.lethal}")

class Clinic(Animal):
    def animal_information(self):
        print(f"This is a {self.animal_type} from {self.region}")
    
    def search(self, animals):
        region = input("Enter a region: ").lower()
        for animal in animals:
            if animal.region == region:
                print(f"Species: {animal.animal_type}")

animals = []
amount_animals = int(input("Enter number of animals: "))
for i in range(amount_animals):
    region = input("Enter a region: ").lower()
    species = input("Enter a species: ").lower()
    color = input("Enter a color: ").lower()
    lethal= input("Is it dangerous: ").lower()
    lethal = lethal == 'yes'

    animal= Animal(region, species, color, lethal)
    animals.append(animal)

clinic = Clinic("asia", "tiger", "orange", "True")

clinic.animal_bio()
clinic.animal_information()
clinic.search(animals)
