""""""

from helper_functions.get_strings import get_strings
from helper_functions.get_floats import get_cash_amount
from helper_functions.typr import typr
from helper_functions.cashyr import cashyr

from helper_functions.authenticators import func_pack

class User:
    """ User super class. Contains and manages name, pin, and password attributes"""
    def __init__(self, name: str, pin: int, password: str):
        self. name = name
        self.pin = pin
        self.password = func_pack(password)

        

    @get_strings("pin")
    def check_pin(self, entered_pin: str=None):
        if self.pin != entered_pin:
            return False
        typr("PIN entry valid.")
        return True

    # @get_strings("name") uses get_strings's decorator_get_name.
    # pre validates (within min and max length, only letters or spaces) a name and passes it as new_name
    @get_strings("name")
    def change_name(self, new_name: str = None):
        """"""
        if new_name == None or new_name == self.name:
            typr(f"Your name '{self.name}' will remain unchanged.")
            typr("Please try again later.")
            return False
        
        self.name = new_name
        typr(f"Your name has been changed to {self.name}.")
        return True
    

    # needs doc string
    @get_strings("pin")
    def change_pin(self, new_pin: str = None):
        if new_pin == None or new_pin == self.pin:
            typr("Your PIN will remain unchanged.")
            typr("Please try again later.")
            return False
        
        self.pin = new_pin
        typr(f"Your new pin is {self.pin}.")
        return True
        # print a do not share pin with anyone message
    

    @get_strings("password")
    def change_password(self, new_password: str = None):
        if new_password == None or new_password == self.password:
            typr("Your password will remain unchanged.")
            typr("Please try again later.")
            return False
        
        self.password = new_password
        typr("Your password has been updated.")
        return True


class BankUser(User):
    """"""
    def __init__(self, name: str, pin: int, password: str):
        super().__init__(name, pin, password)
        self.balance = 0
    

    def show_balance(self):
        typr(f"{self.name} has a balance of ${self.balance:,.2f}.")


    @get_cash_amount
    def deposit(self, cash_amount: float = None):
        if cash_amount == None:
            typr("Deposit failed. Returning to menu.")
            return False
        
        self.balance += cash_amount
        cashyr(cash_amount)
        typr(f"${cash_amount:,.2f} added. ", "fast", False)
        self.show_balance()
        return True
    

    @get_cash_amount
    def withdraw(self, cash_amount: float = None):
        if cash_amount == None:
            typr("Withdraw failed. Returning to menu.")
            return None
        if cash_amount > self.balance:
            typr(f"Cannot withdraw ${cash_amount:,.2f}, insufficient funds.")
            self.show_balance()
            return None
        
        self.balance -= cash_amount
        cashyr(cash_amount)
        self.show_balance()
        return cash_amount
    

    def transfer_money(self, receiving_user = None, cash_amount: float = None, ):
        if receiving_user == None:
            typr("The account you are trying to transfer to does not exist.")
            return False
        
        typr("Enter your PIN: ", "fast", False)
        if self.check_pin():
            typr("Enter amount to transfer: $", "fast", False)
            cash_amount = self.withdraw()
            if cash_amount is not None:
                typr(f"Sending money to {receiving_user.name}")
                receiving_user.deposit(cash_amount)
                return True
        
        typr(f"Transfer to {receiving_user.name} failed.")
        return False