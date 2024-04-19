# This is the second part on OOP Concept and I will try to understand/explore few more concepts like Inheritance, encapsulation, Abstraction, Polymorphism,Method Overriding, Method Overloading,Instance Variables vs Class Variables,Getter and Setter Methods,Class Methods and Static Methods,Dunder (Magic) Methods


# We will create a Super Class for Vehicles also known as Parent class- the attributes in this class can be used for sub-classes or child classes. Vehicle can be any generic vehicle with set of attributes.
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year    
        self._mileage = 0   # notice the _ in mileage: This is Encapsulation concept, it is a private attribute which means that the attribute should not be accessed directly from outside the class. Instead, access to the attribute is controlled through methods (such as getter and setter methods) defined within the class.

    def get_mileage(self):# Getter method to access the private _mileage attribute
        return self._mileage
    
    def set_mileage(self, mileage): # # Setter method to set the mileage attribute
        if mileage >= 0:
            self._mileage = mileage
        else:
            raise ValueError("Mileage cannot be negative")
        

    @classmethod  ##This is a decorator used to define a class method in Python. A class method receives the class itself (cls) as the first argument instead of an (self).
    def get_class_info(cls):
        return f"This is a {cls.__name__} class"

    @staticmethod #he honk method is a static method that simulates a vehicle horn sound. It does not require access to instance attributes(Self) or class-level data(cls)
    def honk():
        return "Beep Beep!"

    def __str__(self): #The purpose of the __str__ method is to provide a human-readable string representation of the object. In this case, it returns a formatted string that represents the vehicle's details 
        return f"{self.year} {self.brand} {self.model}"

    def __len__(self): #This is another special method, known as a "dunder" method, used to customize the behavior of the len() function when applied to an object.
        return 0  

# Derived class - Car (inherits from Vehicle- Self explanatory) 
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def drive(self, miles):
        self._mileage += miles


# Derived class - Truck (inherits from Vehicle, similar to car and truck classes, we can create motorbikes or vans etc)
class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def load(self, weight):
        return f"Loaded {weight} lbs into the truck"


# Here will explore the OOP concepts, lets assign the variables
car = Car("Toyota", "Camry", 2022, "Gasoline")
truck = Truck("Ford", "F-150", 2023, 2000)

# Polymorphism: Using overridden methods
print(car)          # Output will be: 2022 Toyota Camry
print(len(truck))   # Output will be: 0 (for demonstration)

# Encapsulation: Accessing and setting mileage using getter/setter methods
car.set_mileage(5000)
print(car.get_mileage())  # Output will be: 5000

# Class methods and static methods
print(car.get_class_info())  # Output will be: This is a Car class
print(Vehicle.honk())        # Output will be: Beep Beep!

# Inheritance: Truck inherits attributes and methods from Vehicle
print(truck.brand)           # Output will be: Ford
print(truck.payload_capacity)  # Output will be: 2000

# Abstraction: Hiding complex vehicle details and exposing essential attributes/methods
print(truck.year)            # Output will be: 2023
print(car.fuel_type)         # Output will be: Gasoline


'''Summary of above code OOP Concepts
1. Inheritance: Imagine you have a main blueprint for vehicles (like cars or trucks). The main blueprint has basic details that all vehicles share, such as brand, model, and year. Other blueprints (like for cars or trucks) can inherit these details and add more specific things like fuel type for cars or payload capacity for trucks.

2. Encapsulation: This is like putting certain information into a box that only certain parts of the program can access. In the example, the mileage of the vehicle is kept private (or hidden) inside the vehicle class. We can only access or change it using special methods (like get_mileage() and set_mileage()).

3. Abstraction: This means hiding complex details and showing only what's necessary. For instance, when using a vehicle object, you don't need to know all the intricate details of how it works internally; you just need to know basic things like its brand or year.

4. Polymorphism: This is a fancy word that means using the same method in different ways for different objects. For example, when you print a car or a truck, even though they are different types of vehicles, they can both be printed using the same print() function.

5. Method Overriding: This is when a subclass (like a car or truck) has a method with the same name as a method in its parent class (like vehicle), but it behaves differently. For example, a car's drive() method might increase its mileage when called.

6. Class Methods and Static Methods: These are special methods in a class. Class methods are like shared methods among all instances of a class, while static methods are standalone and don't depend on the class state.

7. Getter and Setter Methods: These are methods used to access and modify private attributes of a class, like the _mileage attribute in our vehicle class.

In the example given, we have a Vehicle class that represents a generic vehicle, and subclasses Car and Truck that inherit from Vehicle. Each subclass has its own specific attributes and methods, while still benefiting from the common features provided by the Vehicle class.

For instance, a Car has a drive() method to increase its mileage, and a Truck has a load() method to manage its payload capacity. We can create instances (or objects) of these classes, set their attributes, and use their methods to interact with them, all based on these OOP principles.'''