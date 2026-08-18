def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Error: Book ID {book_id} does not exist in the catalog.")
    elif book_id in borrowed_books:
        print(f"Error: Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Book ID {book_id} ('{catalog[book_id][0]}') borrowed successfully.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Error: Book ID {book_id} was not in the borrowed list.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\n--- Available Books ---")
    available_found = False
    for book_id, (title, author, year) in catalog.items():
        if book_id not in borrowed_books:
            print(f"ID: {book_id} | Title: {title} | Author: {author} | Year: {year}")
            available_found = True
    
    if not available_found:
        print("No books available.")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "1984", "George Orwell", 1949)
    add_book(catalog, 103, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 104, "Moby Dick", "Herman Melville", 1851)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M001")
    register_member(members, "M003")

    print(f"Registered Members (Set count: {len(members)}): {members}\n")

    borrow_book(catalog, borrowed_books, 102)
    borrow_book(catalog, borrowed_books, 104)

    print()
    return_book(borrowed_books, 102)

    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()