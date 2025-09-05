from Models.library import Library
from Models.book import Book
from Models.user import User

if __name__ == "__main__":
    # Create a library
    my_library = Library("City Central")

    # Test fee property
    print("\n--- Library Fee Tests ---")
    print(f"Default monthly fee: Rs.{my_library.fee_per_month}")
    
    # Try setting a new fee
    my_library.fee_per_month = 600
    print(f"Updated monthly fee: Rs.{my_library.fee_per_month}")
    
    # Try setting invalid fee (should raise error)
    try:
        my_library.fee_per_month = -100
    except ValueError as e:
        print(f"Setting negative fee failed as expected: {e}")

    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("Pride and Prejudice", "Jane Austen")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger")

    # Add books
    for book in [book1, book2, book3, book4]:
        my_library.add_book(book)

    # Create and register valid users
    users = []
    try:
        user1 = User("Alice", 23, 1)
        users.append(user1)
        my_library.register_user(user1)
        
        user2 = User("Bob", 25, 2)
        users.append(user2)
        my_library.register_user(user2)
        
        print("\n--- Testing underage user registration ---")
        user3 = User("Charlie", 12, 3)  # 🚨 Will raise ValueError
        users.append(user3)
        my_library.register_user(user3)
    except ValueError as e:
        print(f"User creation failed: {e}")

    if users:  # Only run tests if we have valid users
        print("\n--- Property Checks ---")
        # ✅ Age validation works
        print(f"{users[0].name}'s age: {users[0].age_res}")
        try:
            users[0].age_res = 15   # 🚨 should raise ValueError
        except ValueError as e:
            print(f"Failed to update age: {e}")

        print("\n--- Borrowing Tests ---")
        # Test initial borrow
        print(f"Can {users[0].name} borrow books? {users[0].can_borrow}")
        users[0].borrow_book(book1)   # Alice borrows first book
        print(f"Can {users[0].name} borrow more books now? {users[0].can_borrow}")

        # Test waiting list functionality
        users[1].borrow_book(book1)  # Bob should be added to waiting list
        
        # Test return and automatic assignment to next in queue
        users[0].return_book(book1)  # Alice returns, should be automatically given to Bob
        
        # Test borrow limit
        print("\n--- Testing Borrow Limit ---")
        users[0].borrow_book(book1)  # Borrow first book
        users[0].borrow_book(book2)  # Borrow second book
        users[0].borrow_book(book3)  # Borrow third book (should work)
        users[0].borrow_book(book4)  # Try to borrow fourth book (should fail)

        # Test history functionality
        print(f"\n--- Borrowing History ---")
        print(f"Last book borrowed by {users[0].name}: {users[0].last_borrowed()}")
        print(f"{users[0].name}'s full borrowing history: {', '.join(str(book) for book in users[0].borrowing_history())}")
