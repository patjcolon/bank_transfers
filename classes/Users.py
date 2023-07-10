"""Classes for bank users with functionality for changing account info and managing money
User super class that takes care of name, pin, and password.
BankUser sub class adds a balance attribute. with balance it adds functionality for withdraw, 
deposit, check balance, and send and request cash.
by patjcolon
Last Updated 7/9/2023"""

from helper_functions.get_strings import get_strings
from helper_functions.get_floats import get_cash_amount
from helper_functions.typr import typr
from helper_functions.cashyr import cashyr

from helper_functions.authenticators import func_pack

class User:
    """ User super class. Contains and manages name, pin, and password attributes
    name, pin, and password can be changed with User methods"""
    def __init__(self, name: str, pin: int, password: str):
        self. name = name
        self.pin = pin
        self.password = password

        
    @get_strings("pin")
    def check_pin(self, entered_pin: str=None):
        """pin verification used for authenticating money transfers"""
        if self.pin != entered_pin:
            return False
        typr("PIN entry valid.")
        return True
    
    @get_strings("password")
    def check_password(self, entered_password: str=None):
        """password verification used for authenticating money transfers"""
        if self.password != entered_password:
            return False
        typr("Password is correct.")
        return True


    # @get_strings("name") uses get_strings's decorator_get_name.
    @get_strings("name")
    def change_name(self, new_name: str = None):
        """allows user to change name. 
        pre validates (within min and max length, only letters or spaces) a name and passes it as new_name"""
        if new_name == None or new_name == self.name:
            typr(f"Your name '{self.name}' will remain unchanged.")
            typr("Please try again later.")
            return False
        
        self.name = new_name
        typr(f"Your name has been changed to {self.name}.")
        return True
    

    @get_strings("pin")
    def change_pin(self, new_pin: str = None):
        """allows user to change pin
        pre validates a pin and passes it as new pin"""
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
        """allows uer to change password
        pre validates a password and checks if it is different. if conditions are met new password is updated"""
        if new_password == None or new_password == self.password:
            typr("Your password will remain unchanged.")
            typr("Please try again later.")
            return False
        
        self.password = new_password
        typr("Your password has been updated.")
        return True


class BankUser(User):
    """Subclass of User, adds balance attribute and methods influencing it
    can deposit, withdraw, transfer and request money"""
    def __init__(self, name: str, pin: int, password: str):
        super().__init__(name, pin, password)
        self.balance = 0
    

    def show_balance(self):
        """shows bankuser balance"""
        typr(f"{self.name} has a balance of ${self.balance:,.2f}.")


    @get_cash_amount
    def deposit(self, cash_amount: float = None):
        """allows bankuser to deposit cash, minimum of a penny"""
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
        """allows bankuser to withdraw cash
        minimum allowable valid withdraw is 1 penny, up to the amount of their balance as maximum"""
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
    

    def transfer_money(self, receiving_user = None, cash_amount: float = None):
        """allows bankuser to send cash to another bankuser. 
        rules of withdraw apply here, and must validate transfer by confirming with PIN"""
        if receiving_user == None:
            typr("The account you are trying to transfer to does not exist.")
            return False
        
        typr(f"Enter {self.name}'s PIN: ", "fast", False)
        if self.check_pin():
            if not cash_amount: typr("Enter amount to transfer: $", "fast", False)
            cash_amount = self.withdraw(cash_amount)
            if cash_amount is not None:
                typr(f"Sending money to {receiving_user.name}...")
                receiving_user.deposit(cash_amount)
                return True
        
        typr(f"Transfer to {receiving_user.name} failed.")
        return False


    def request_money(self, sending_user = None, cash_amount: float = None):
        """allows bankuser to request money from another bankuser
        requesting user must provide pin of requested user, as well as their
        own password. if both are validated, transfer will take place if the 
        sending user has funds available in balance"""
        if sending_user == None:
            typr("The account you are trying to request payment from does not exist.")
            return False
        
        typr(f"Enter {sending_user.name}'s PIN: ", "fast", False)
        if not sending_user.check_pin():
            typr("PIN was incorrect. Payment request failed.")
            return False

        typr(f"Enter {self.name}'s password: ", "fast", False)
        if not self.check_password():
            typr("Password is incorrect. Payment request failed.")
            return False
        
        typr("Accounts info validated... Proceeding to payment request...")
        if not cash_amount: typr("Enter amount to transfer: $", "fast", False)
        cash_amount = sending_user.withdraw(cash_amount)
        if cash_amount is not None:
            typr(f"Sending money to {self.name}...")
            self.deposit(cash_amount)
            return True

