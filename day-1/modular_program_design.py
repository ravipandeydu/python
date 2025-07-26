def add_book(library):
    """
    Adds a new book to the library inventory.

    Args:
        library (list): The list representing the library's inventory.
                        Each book is a dictionary with keys 'title', 'author', 'isbn'.
    """
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    isbn = input("Enter book ISBN: ").strip()

    if not title or not author or not isbn:
        print("Error: All fields (title, author, ISBN) are required.")
        return

    # Check if a book with the same ISBN already exists
    for book in library:
        if book['isbn'].lower() == isbn.lower():
            print(f"Error: A book with ISBN '{isbn}' already exists in the library.")
            return

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn
    }
    library.append(new_book)
    print(f"Book '{title}' added successfully!")

def search_book(library):
    """
    Searches for books in the library by title or author.

    Args:
        library (list): The list representing the library's inventory.
    """
    print("\n--- Search Book ---")
    query = input("Enter title or author to search: ").strip().lower()

    if not query:
        print("Please enter a search query.")
        return

    found_books = []
    for book in library:
        if query in book['title'].lower() or query in book['author'].lower():
            found_books.append(book)

    if found_books:
        print("\n--- Search Results ---")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
    else:
        print(f"No books found matching '{query}'.")

def display_inventory(library):
    """
    Displays all books currently in the library inventory.

    Args:
        library (list): The list representing the library's inventory.
    """
    print("\n--- Library Inventory ---")
    if not library:
        print("The library is currently empty.")
        return

    for i, book in enumerate(library):
        print(f"{i+1}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

def main():
    """
    Main function to run the library management system.
    Handles user interaction and calls other functions.
    """
    # Initialize an empty list to store books
    library_inventory = []

    while True:
        print("\n--- Library Management System Menu ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_book(library_inventory)
        elif choice == '2':
            search_book(library_inventory)
        elif choice == '3':
            display_inventory(library_inventory)
        elif choice == '4':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()