# Lets understand Tight Coupling Design :In this example, we'll start with tightly coupled classes, where the Book class directly references the Author class, leading to high dependency and tight coupling between them.

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author_name):
        self.title = title
        self.author = Author(author_name)  # Creating Author instance inside Book, This tight coupling means that any changes to the Author class can directly impact the Book class, making the code less flexible and harder to maintain.
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print("----")

# Creating a Book instance
book1 = Book("Harry Potter", "J.K. Rowling")

# Displaying book information
book1.display_info()

##### Solution to this is to create another class for Author and pass the author class  as a parameter ##

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print("----")


# Creating an Author instance
author1 = Author("J.K. Rowling")

# Creating a Book instance and passing Author instance
book1 = Book("Harry Potter", author1)

# Displaying book information
book1.display_info()

