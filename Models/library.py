from .user import User,PremiumUser
from .Payments import Payment

class Library:
    _base_fee_per_month = 500 

    def __init__(self,name):
        self.name = name
        self.books=[]
        self.users = []
        self._fee_per_month = self._base_fee_per_month  
    
    @property
    def fee_per_month(self):
        """Get the current monthly fee"""
        return self._fee_per_month
    
    @fee_per_month.setter
    def fee_per_month(self, value):
        """Set the monthly fee with validation"""
        if value < 0:
            raise ValueError("Fee cannot be negative")
        self._fee_per_month = value
    
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
    
    @property
    def paid_fee(self):
        return ""
    
    def register_user(self,user,payment_method: Payment):
        fee_to_pay = self._fee_per_month

        if isinstance(user,PremiumUser):
            fee_to_pay = user.get_discount_fee(self._fee_per_month)
        
        payment_method.pay(fee_to_pay)
        self.users.append(user)
        print(f"Registered user {user.name} with monthly fee of Rs.{self.fee_per_month}")
    
    def find_user(self,user_id):
        for user in self.users:
            if user.user_ID == user_id:
                return user
        return None

    def __str__(self):
        return f"{self.name} Library"
    
    def __getitem__(self,key):
        if isinstance(key,int):
            return self.users[key]
        elif isinstance(key,str):
            for user in self.users:
                if user.name.lower() == key.lower():
                    return user
            raise KeyError(f"No user with name '{key}' found")
        else:
            raise TypeError("Key must be int (index) or str (username)")
    
    def __setitem__(self, key, value):
        if isinstance(key, int):  
            self.users[key] = value
        elif isinstance(key, str):  
            for i, user in enumerate(self.users):
                if user.name.lower() == key.lower():
                    self.users[i] = value
                    return
            raise KeyError(f"No user with name '{key}' found")
        else:
            raise TypeError("Key must be int (index) or str (username)")

    
