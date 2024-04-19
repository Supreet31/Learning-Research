# I wanted to understand OOP concept, so I created a simple program in which a user will select a planet and the program will spit out certain facts about that planet. In this way I will add comments for each concept for better understanding.

#To do this we will first define the Planet class, which serves as a blueprint for creating planet object.
#Then we will add its atrributes using Constructor method (__init__) for initializing a new Planet object. 
class Planet:
    def __init__(self, name, radius, mass, color=None, distance_from_earth=None):
        self.name = name
        self.radius = radius  
        self.mass = mass      
        self.color = color    
        self.distance_from_earth = distance_from_earth  
        
##****************************************************************************##
    def convert_mass(self):
        #Method to convert the mass of the planet into a more readable format.
        if self.mass >= 1e9:
            return f"{self.mass / 1e9:.2f} billion km³"
        elif self.mass >= 1e6:
            return f"{self.mass / 1e6:.2f} million km³"
        else:
            return f"{self.mass:.2f} km³"
        
##****************************************************************************##
    def display_info(self):
        #Method to display detailed information about the planet.
        print(f"Planet Information:")
        print(f"Name: {self.name}")
        print(f"Radius: {self.radius} km")
        print(f"Mass: {self.convert_mass()}")
        if self.color:
            print(f"Color: {self.color}")
        if self.distance_from_earth:
            print(f"Distance from Earth: {self.distance_from_earth} km")

# Dictionary to store planet information (name, radius in km, mass in kg, color, distance from Earth in km)
planets_data = {
    "Mercury": (2439.7, 3.3011e23, "gray", 91691000),
    "Venus": (6051.8, 4.8675e24, "yellowish", 41400000),
    "Earth": (6371, 5.972e24, "blue", 0),
    "Mars": (3389.5, 6.4171e23, "reddish", 78340000),
    "Jupiter": (69911, 1.8982e27, "orange and white", 628730000),
    "Saturn": (58232, 5.6834e26, "pale gold", 1275000000),
    "Uranus": (25362, 8.6810e25, "pale blue", 2723950000),
    "Neptune": (24622, 1.02413e26, "deep blue", 4351400000)
}

# Get user input for the planet-
print("Select a planet from the following list:")
for index, planet in enumerate(planets_data.keys()):  
    print(f"{index + 1}. {planet}")
    #enumerate() is a built-in Python function used to iterate over a sequence
    # check this link for information on Python dictionary  https://developers.google.com/edu/python/dict-files

try:
    choice = int(input("Enter the number of the planet: "))
    planet_names = list(planets_data.keys())
    selected_planet = planet_names[choice - 1]

    # Create a Planet object based on user's selection
    radius, mass, color, distance = planets_data[selected_planet]
    planet = Planet(selected_planet, radius, mass, color, distance)

    # Display planet information
    planet.display_info()

except (ValueError, IndexError):
    print("Invalid choice. Please enter a valid number corresponding to a planet.")


''' Summary:
In this program, we explored OOP concepts. OOP is a way to organize your code around real-world objects, like planets in our case. 
Breakdown:
We started by defining a blueprint for our planet object using a class called Planet. A class is like a recipe for making objects.
Attributes and Constructor Method: Inside the Planet class, we defined attributes (characteristics) such as name, radius, mass, color, and distance_from_earth. These are the properties that describe a planet. 
The __init__ method (constructor) helps set up these attributes when a new planet object is created.
Later, We added methods (functions inside a class:Planet) like convert_mass and display_info. These methods allow us to perform actions related to our planet object, such as converting the mass into a readable format (convert_mass method) and displaying detailed information about the planet (display_info method).
Using the Planet Class: We used the Planet class to create planet objects based on user input. When a user selects a planet, we fetch its data from a dictionary (planets_data) and then create a new Planet object with the appropriate attributes.
Displaying Planet Information: Finally, we display detailed information about the selected planet using the display_info method of the Planet object.
OOP CONCEPTS : CLASS, OBJECT,METHODS, CONSTRUCTOR'''