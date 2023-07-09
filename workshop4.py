"""Workshop 4 Project
Create a bank account app that uses classes to represent users and accounts
has a way to a transfer and request money
by patjcolon
Last updated: 7/8/2023
"""
from classes.Users import BankUser
from helper_functions.typr import typr

# # # to do:
# come back and document everything
# make modules for every object and one+ for helper functions. app.py is running menu 
# class User
# class BankUser(User)
# observer class to send notifications from one user to another user


# input decorator factory that can get different types of input depending on what's needed
# @get_strings('user_name')    <- how to decorate a function/method








user1 = BankUser("tim", 1234, "pass")


user1.show_balance()
typr("Enter amount to deposit: $", "fast", False)
user1.deposit()
typr("Enter amount to deposit: $", "fast", False)
user1.deposit()
typr("Enter amount to withdraw: $", "fast", False)
user1.withdraw()

typr("Enter new name: ", "fast", False)
user1.change_name()
typr("Enter new PIN: ", "fast", False)
user1.change_pin()

typr("Enter amount to deposit: $", "fast", False)
user1.deposit()
user1.show_balance()

""" Driver Code for Task 1 """
# test_user = User("Bob", 1234, "password")
# typr(f"DC Task 1 test: {test_user.name} {test_user.pin} {test_user.password}")