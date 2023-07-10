'''
String obfuscation challenge example
By Jack Seymour and patjcolon
Data 7/9/2023

Challenge:
    Create a function that will obfuscate a string that can be unpacked with the provided function
    Function takes a string as an argument
    Function returns a list
'''
from getpass import getpass
# from functools import wraps  <- for login authenticator. not implemented


def func_unpack(_data):
    '''Unpacking function
    takes a list of numbers and reverts packing done using bitwise xor operator,
    which is repeatable and reversible with the right pattern. compares to iteration of i=0 i+=1'''
    i = 0
    out_string = ""
    for _chr in _data:
        out_string = out_string + chr(_chr ^ i)
        i += 1
    return out_string


def func_pack(_string):
    '''Packing function
    takes a string character by character and turns it into ascii decimal value representation
    iterates through i=0 i+=1 using bitwise xor to compare and modify the binary representation
     of the decimal value representation of the character in a reversible way '''
    i = 0
    out_data = []
    for _chr in _string:
        out_data.append(ord(_chr) ^ i)
        i += 1
    return out_data


# test dict for login_authenticator
accounts = {
           "patjcolon": "pass123",
           "lolyngee": "1224"
           }

# not used. 
def login_authenticator(function):
    """login authentication decorator that runs user input against database entry"""
    def processor():
        username = input("What is your username? \n> ")
        password = getpass("What is your password? \n> ")
        try:
            if password == accounts[username]:
                function()
            else:
                print("Password is incorrect.")
        except KeyError:
            print(f"No account with username \"{username}\".")
    return processor
