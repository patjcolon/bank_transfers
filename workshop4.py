"""Workshop 4 Project
this app allows bankaccount users to be able to handle their money and make transfers to each other
by patjcolon
Last updated: 7/8/2023
"""
from classes.Users import BankUser
from helper_functions.typr import hide_unhide
# from classes.ContextManagers import test_name
from helper_functions.authenticators import func_pack

# # # to do:
# come back and document everything
# make modules for every object and one+ for helper functions. app.py is running menu 
# observer class to send notifications from one user to another user

#test_name() <- context manager import. unfinished/canceled



# if i was able to make a way to create accounts, accounts created would have their
# passwords run through func_pack, without the user's knowledge.
# however these are test accounts and i did not make a way to organically create accounts,
# so these test passwords are simulated database passwords
test_password1 = func_pack("passWORD")
test_password2 = func_pack("password123")

# test user 1 and 2. user2 will have 500k added to account balance
#then send 50k to user1, then user2 will request all but 1 penny back from user1
user1 = BankUser("Pat Pat", "1234", test_password1)
user2 = BankUser("Lara C", "0000", test_password2)

hide_unhide() # hides terminal cursor
user2.deposit(500000)
user1.show_balance()
user2.transfer_money(user1, 50000)
user2.request_money(user1, 49999.99)

user1.show_balance()
user2.show_balance()