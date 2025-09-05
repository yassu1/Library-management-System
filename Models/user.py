class User:
    def __init__(self, name, age, user_ID, max_limit=3):
        self.name = name
        self.age_res = age
        self.user_ID = user_ID
        self.borrowing_service = BorrowingService(max_limit)

    @property
    def age_res(self):
        return self._age
    
    @age_res.setter
    def age_res(self, value):
        if value < 18:
            raise ValueError("Not allowed under age 18")
        self._age = value

    def borrow_book(self, book):
        self.borrowing_service.borrow_book(self, book)

    def return_book(self, book):
        self.borrowing_service.return_book(self, book)

    def last_borrowed(self):
        return self.borrowing_service.last_borrowed()

    def borrowing_history(self):
        return self.borrowing_service.history

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"User('{self.name}', '{self.user_ID}')"


class BorrowingService:
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.borrowed_books = []
        self.history = []

    @property
    def can_borrow(self):
        return len(self.borrowed_books) < self.max_limit

    def borrow_book(self, user, book):
        if not self.can_borrow:
            print(f"{user.name} cannot borrow more than {self.max_limit} books")
            return
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            self.history.append(book)
            print(f"{user.name} borrowed {book.title}")
        else:
            book.add_to_waiting_list(user)

    def return_book(self, user, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{user.name} returned {book.title}")

            next_user = book.next_in_queue()
            if next_user:
                print(f"{book.title} is now assigned to {next_user.name}")
                next_user.borrow_book(book)
        else:
            print(f"{user.name} did not borrow {book.title}")

    def last_borrowed(self):
        return self.history[-1] if self.history else None



class Teacher(User):
    def __init__(self, name, age, user_ID, subject):
        super().__init__(name, age, user_ID, max_limit=5)
        self.subject = subject

    def borrow_book(self, book):
        print(f"Teacher {self.name} is borrowing {book.title}")
        super().borrow_book(book)

    def __str__(self):
        return f"Teacher {self.name} teaches {self.subject}"


class GuestUser(User):
    def __init__(self, name, age, user_ID):
        super().__init__(name, age, user_ID, max_limit=1)

    def borrow_book(self, book):
        print(f"Guest {self.name} is borrowing {book.title}")
        super().borrow_book(book)

    def __str__(self):
        return f"Welcome {self.name} to the Library"


class Donor:
    def donate(self, amount):
        print(f"Thanks for donating {amount}")


class PremiumUser(User, Donor):
    Discount_Rate = 0.2

    def __init__(self, name, age, user_ID):
        super().__init__(name, age, user_ID, max_limit=10)

    def borrow_book(self, book):
        print(f"Premium user {self.name} has special access!")
        super().borrow_book(book)

    def get_discount_fee(self, base_fee):
        return base_fee * (1 - self.Discount_Rate)

    def __str__(self):
        return f"Welcome Premium Member {self.name}"
