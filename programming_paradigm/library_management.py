class Book:
    def __init__(self, title, author):
        # Check for correct initialization
        assert isinstance(title, str), "Title must be a string"
        assert isinstance(author, str), "Author must be a string"
        self.title = title
        self.author = author
        self._is_checked_out = False  # Book is available initially
    
    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if self._is_checked_out:
            print(f"The book '{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"You've checked out '{self.title}' by {self.author}.")
    
    def return_book(self):
        """Return the book, marking it as available."""
        if not self._is_checked_out:
            print(f"The book '{self.title}' is already available.")
        else:
            self._is_checked_out = False
            print(f"You've returned '{self.title}' by {self.author}.")
    
    def is_available(self):
        """Return if the book is available."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        # Initial check for Library class instantiation
        self._books = []  # List to store books
    
    def add_book(self, book):
        """Add a book to the library."""
        if not isinstance(book, Book):
            raise ValueError("Only instances of Book can be added to the library.")
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"Sorry, '{title}' is currently checked out.")
                return
        print(f"Book '{title}' not found in the library.")
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")
    
    def list_available_books(self):
        """List all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books in the library.")


