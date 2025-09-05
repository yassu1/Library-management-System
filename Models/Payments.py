from abc import ABC,abstractmethod

class Payment(ABC):
    
    @property
    @abstractmethod
    def transaction_fee(self):
        """Every payment method must define its fee"""
        pass


    @abstractmethod
    def pay(self,amount):
        pass
    
class UPI(Payment):

    @property
    def transcation_fee(self):
        return 0

    def pay(self,amount):
        print(f"Paid {amount} using UPI (Fee. {self.transcation_fee})")
