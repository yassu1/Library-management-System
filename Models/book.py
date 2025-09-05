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
    