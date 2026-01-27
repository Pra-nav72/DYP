# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return self.title, self.author

# Library class (contains Book object)
class Library:
    def __init__(self, book):
        self.book = book

    def display_book_details(self):
        title, author = self.book.get_details()
        print("Book Title:", title)
        print("Author:", author)

# Creating Book object
b1 = Book("The Alchemist", "Paulo Coelho")

# Passing Book object to Library (containership)
lib = Library(b1)

# Displaying book details using Library class
lib.display_book_details()
