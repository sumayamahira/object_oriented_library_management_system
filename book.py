class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def book_borrow(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed.")
        else:
            print("It's already borrowed.")

    def book_return(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned.")

        else:
            print("The book was not borrowed, Book is already available.")


