class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, book_title):
        for item in self.books:
            if item.title == book_title:
                self.books.remove(item)
                print("Book removed successfully.")
                return
        print("Book is not found.")

    def search_book(self, book_title):
        for item in self.books:
            if item.title == book_title:
                print("Book found.")
                return item

        print("Book not found.")

    def show_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for item in self.books:
            print(f"Title: {item.title}, Author: {item.author}, Status: {item.is_available}")

    def borrow_book(self, book_title):
        book_search = self.search_book(book_title)
        if book_search:
            book_search.book_borrow()

    def return_book(self, book_title):
        book_search = self.search_book(book_title)
        if book_search:
            book_search.book_return()
