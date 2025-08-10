from library_management import Library

def main():
    library = Library()

    while True:
        print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. List Books\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
            print("Book added.")
        elif choice == "2":
            title = input("Enter title to borrow: ")
            if library.borrow_book(title):
                print("Book borrowed.")
            else:
                print("Book not available.")
        elif choice == "3":
            title = input("Enter title to return: ")
            if library.return_book(title):
                print("Book returned.")
            else:
                print("Book not found or not borrowed.")
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
