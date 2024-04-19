# DUPLICATION :In this code, we have separate functions (input_book_info and display_book_info) duplicating similar code for handling book information.

def input_book_info():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    return title, author

def display_book_info(title, author):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print("----")

# Input book information
book_title, book_author = input_book_info()

# Display book information
display_book_info(book_title, book_author)

#Good Example 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("----")

# Function to create a new Book instance
def create_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    return Book(title, author)

# Function to display information about a book
def show_book_info(book):
    book.display_info()

# Usage Example:
# Create a new Book instance
book1 = create_book()

# Display information about the book
show_book_info(book1)

'''
Efficiency: By writing reusable functions and classes, we save time and effort by not duplicating similar code across our program.
Maintainability: Reusable code is easier to maintain and update. Changes made to a single function or class propagate to all places where it's used.
Readability: Eliminating duplication makes our code cleaner and more readable, as it focuses on the logic of what needs to be done rather than repetitive implementation details.
'''
