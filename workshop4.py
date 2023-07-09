"""Workshop 4 Project
Create a bank account app that uses classes to represent users and accounts
has a way to a transfer and request money
by patjcolon
Last updated: 7/8/2023
"""
from classes.Users import BankUser
from helper_functions.typr import typr
from classes.ContextManagers import test_name

# # # to do:
# come back and document everything
# make modules for every object and one+ for helper functions. app.py is running menu 
# class User
# class BankUser(User)
# observer class to send notifications from one user to another user


# input decorator factory that can get different types of input depending on what's needed
# @get_strings('user_name')    <- how to decorate a function/method





test_name()


user1 = BankUser("Pat Pat", "1234", "pass")
user2 = BankUser("Lara C", "0000", "pass")

typr("Enter new password: ", "fast", False)
user1.change_password()
print(user1.password)