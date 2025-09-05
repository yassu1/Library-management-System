from collections import deque

class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
        self.waiting_list = deque()
    
    def add_to_waiting_list(self,user):
        if user not in self.waiting_list:
            self.waiting_list.append(user)
            print(f"{user.name} added to waiting list for {self.title}")
        else:
            print(f"{user.name} is already in the waiting list for {self.title}")

    def next_in_queue(self):
        return self.waiting_list.popleft() if self.waiting_list else None
    
    def __str__(self):
        return f"{self.title}"
    
    def __repr__(self):
        return f"Book('{self.title}','{self.author}')"
    
class user:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        self.history = []
    
    def borrow_book(self,book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            self.history.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:   
            book.add_to_waiting_list(self)
    
    def return_book(self,book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")

            next_user = book.next_in_queue()
            if next_user:
                print(f"{book.title} is now assigned to {next_user.name} from waiting list")
                next_user.borrow_book(book)
        else:
            print(f"{self.name} did not borrow {book.title}")
        
    def last_borrowed(self):
        if self.history:
            return self.history[-1]
        return None

    def borrowing_history(self):
        return self.history

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"user('{self.name}','{self.user_id}')"

class Library:
    def __init__(self,name):
        self.name = name
        self.books=[]
        self.users = []
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Added {book.title} to the library")
    
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.title} from the library")
        else:
            print(f"{book.title} is not in the library")    
    
    def search_book(self,title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books
    
    def register_user(self,user):
        self.users.append(user)
        print(f"Registered user {user.name}")
    
    def find_user(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def __str__(self):
        return f"{self.name} Library"
    

if __name__ == "__main__":
    # Create a library
    my_library = Library("City Central")

    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Create users
    user1 = user("Alice", 1)
    user2 = user("Bob", 2)
    user3 = user("Charlie", 3)

    # Register users
    my_library.register_user(user1)
    my_library.register_user(user2)
    my_library.register_user(user3)

    # Borrow logic with waiting list
    user1.borrow_book(book1)   # Alice borrows
    user2.borrow_book(book1)   # Bob joins waiting list
    user3.borrow_book(book1)   # Charlie joins waiting list

    # Alice returns book → Bob should get it automatically
    user1.return_book(book1)

    # Now Bob returns → Charlie should get it automatically
    user2.return_book(book1)