class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def book_borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def book_return(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")

        else:
            print(f"'{self.title}' was not borrowed.")


