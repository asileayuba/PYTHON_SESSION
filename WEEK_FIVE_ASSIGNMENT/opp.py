class Aircraft:
    """
    A class representing an Aircraft.
    """
    def __init__(self, model, manufacturer, capacity):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity

    def display_info(self):
        return f"Model: {self.model}, Manufacturer: {self.manufacturer}, Capacity: {self.capacity} passengers"

    def move(self):
        return "Flying in the skies"

# Inherited class
class FighterJet(Aircraft):
    """
    A class representing a Fighter Jet, inheriting from Aircraft.
    """
    def __init__(self, model, manufacturer, capacity, weapon_type):
        super().__init__(model, manufacturer, capacity)
        self.weapon_type = weapon_type

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Weapon Type: {self.weapon_type}"

    def move(self):
        return "Flying at supersonic speeds"

# Activity 2: Polymorphism Challenge
class Vehicle:
    """
    A general class for vehicles.
    """
    def move(self):
        return "Moving"

class Car(Vehicle):
    """
    A class representing a Car, inheriting from Vehicle.
    """
    def move(self):
        return "Driving"

class Plane(Vehicle):
    """
    A class representing a Plane, inheriting from Vehicle.
    """
    def move(self):
        return "Flying"

class Boat(Vehicle):
    """
    A class representing a Boat, inheriting from Vehicle.
    """
    def move(self):
        return "Sailing"

# Demonstration
if __name__ == "__main__":
    # Activity 1: Create an Aircraft and Fighter Jet
    commercial_plane = Aircraft("A320", "Airbus", 180)
    print(commercial_plane.display_info())
    print(commercial_plane.move())

    fighter = FighterJet("F-16", "Lockheed Martin", 1, "Missiles")
    print(fighter.display_info())
    print(fighter.move())

    # Activity 2: Polymorphism in action
    vehicles = [Car(), Plane(), Boat()]

    for vehicle in vehicles:
        print(vehicle.move())
