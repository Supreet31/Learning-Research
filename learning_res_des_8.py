'''Most of the time, Un testability is caused by tight coupling.
Unit testing is important. If you don’t test your code, you are bound to ship broken code. But still most people do not properly cover their code with tests. Why? Mostly because their code is hard to test.What makes code hard to test? Mainly the previous point: Tight coupling.
Unit testing - it might seem obvious - tests units of code (usually classes). But how can you test individual classes if they are tightly coupled? You probably can somehow, with even more dirty hacks. But people usually do not do those efforts and just leave their code untested and broken.
Whenever you don't write unit tests because you “don’t have time”, the real cause is probably that your code is bad.
If your code is good you can test it in no time. Only with bad code does unit testing becomes a burden.'''

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author_name):
        self.title = title
        self.author = Author(author_name)  # Creating Author instance inside Book
    
    def get_author_name(self):
        return self.author.name

# Creating a Book instance
book1 = Book("Harry Potter", "J.K. Rowling")

# Displaying author name-
print(book1.get_author_name())
