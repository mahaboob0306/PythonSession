#abstract class ,abstract method and concrete method
#json files
from abc import ABC,abstractmethod
#abstract class
class Bankaccount(ABC):
    def __init__(self,account_number,balance):
        self.balance=balance
        self.account_number=account_number
    @abstractmethod
    def calculate_interest(self):#abstract method
        pass#indicate that the method has no implementation in the abstract class itself
#concrete class
class SavingsAccount(Bankaccount):
    def __init__(self, account_number, balance,interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        #return super().calculate_interest()
        interest=self.balance*self.interest_rate
        return interest
#creating objects of concrete class
savings_account=SavingsAccount(1234,5000,0.05)
print("Savings Account Interest",savings_account.calculate_interest())