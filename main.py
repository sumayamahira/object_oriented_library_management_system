from book import Book
from library import Library

library = Library()

while True:
    # CLI menu for library management system
    user_order = input("""
    ===== Library Menu =====
    1. Add book
    2. Borrow book
    3. Return book
    4. Search book
    5. Show all books
    6. Exit
    Pick from this menu: """)

    # debugging for invalid input
    try:
        user_order = int(user_order)
    except ValueError:
        print("Please use a valid numeric input. ex.'1'")
        continue

    if user_order == 1:
        # add book to the library
        book_title = input("What is the Title? \nTitle: ").lower()
        book_author = input("Who is the Author of the particular book? \nAuthor: ").lower()
        book = Book(book_title, book_author)
        library.add_book(book)

    elif user_order == 2:
        # borrow book from the library
        library.borrow_book(input("Which book do you want? \nTitle: ").lower())

    elif user_order == 3:
        # return book to the library
        library.return_book(input("Which book do you want to return? \nTitle: ").lower())

    elif user_order == 4:
        # search book from the library
        library.search_book(input("Which book you are looking for? \nTitle: ").lower())

    elif user_order == 5:
        # show all the books of the library
        library.show_all_books()

    elif user_order == 6:
        # Exit
        print("Exiting... Goodbye!")
        break

    else:
        print("Choose a valid option among 1 to 6.")
