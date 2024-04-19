#Indescriptive Naming :This should be obvious, but still needs to be said: name your classes, methods, attributes, and variables properly. Remember that you write code for people, not for computers. Programming languages are for humans.
#For example, can you guess what the strpbrkLinks to an external site. PHP function does?  Nobody who wants to search a string for a list of characters looks for a function named strpbrk.  This function was inherited from C and its name stands for “string pointer break”, which is not very helpful since the PHP language doesn’t actually have pointers. #The lesson from this: Please, name your classes, methods, and variables properly so that people actually know what you mean.  Functions like strpbrk or variables like $yysstk may be obvious to the author, but also only to the author.

# bad code example #
class B:
    def __init__(self, t, a):
        self.t = t  # Instead of 'title', using 't'
        self.a = a  # Instead of 'author', using 'a'
    
    def info(self):
        print(f"Title: {self.t}")
        print(f"Author: {self.a}")
        print("----")

book2 = B("The Great Gatsby", "F. Scott Fitzgerald")
book2.info()

#Good example- look at the names#

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("----")

# Creating a Book instance
book1 = Book("Harry Potter", "J.K. Rowling")

# Displaying book information using the display_info method.
book1.display_info()
