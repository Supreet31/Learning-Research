# Lets understand Singleton Design :The Singleton syndrome occurs when developers use the Singleton pattern excessively throughout their codebase, often as a default choice without considering alternative patterns or architectural approaches. 


class Book:
    library_book = None  # Private variable to hold the single instance of Book
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @classmethod
    def get_library_book(cls, title, author):
        if not cls.library_book:
            cls.library_book = cls(title, author)
        return cls.library_book
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("----")
        

# Let's create books using the Singleton pattern

# Creating a Book instance
book1 = Book.get_library_book("The Prophet", "Khalil Gibran")

# Accessing the same instance again
book2 = Book.get_library_book("The Great Gatsby", "F. Scott Fitzgerald")

# Both book1 and book2 refer to the same singleton book instance, this is a problem
print("Printing Book 1:")
book1.display_info()

print("Printing Book 2:")
book2.display_info()

# Let's try to create a new Book instance using regular initialization
# This should still refer to the original singleton book instance
book3 = Book("Masnavi", "Rumi")
print("Printing Book 3:")
book3.display_info()

# Checking if book3 is the same singleton book instance as book1 and book2
print("book1 is book3:", book1 is book3)
print("book2 is book3:", book2 is book3)


#Global State: The Singleton pattern introduces global state, which can make the code harder to understand and maintain. Since there is a single instance shared across the application, any changes or side effects caused by this instance can affect different parts of the program unpredictably.
#Coupling and Dependencies: Code that relies heavily on Singletons can become tightly coupled, making it harder to refactor and test components independently. Classes that depend on Singletons directly create tight dependencies, making it difficult to substitute or mock these dependencies during testing.
#Concurrency and Thread Safety: Singleton implementations can introduce challenges related to concurrency and thread safety. In multithreaded environments, developers need to ensure that the Singleton instance is properly synchronized to avoid race conditions and other concurrency issues.
#Testing Complexity: Code built around Singletons can be difficult to test, especially when Singletons are used extensively throughout the codebase. Mocking or substituting Singletons for testing purposes can become cumbersome and may require additional setup.
#Alternative Patterns: In many cases, alternative design patterns or architectural styles may be more suitable than the Singleton pattern. For example, dependency injection (DI) can provide a more flexible and testable approach to managing object dependencies without relying on global state.