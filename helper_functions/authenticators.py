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
from functools import wraps


def func_unpack(_data):
    '''Unpacking function'''
    i = 0
    out_string = ""
    for _chr in _data:
        out_string = out_string + chr(_chr ^ i)
        i += 1
    return out_string


def func_pack(_string):
    '''Packing function'''
    i = 0
    out_data = []
    for _chr in _string:
        out_data.append(ord(_chr) ^ i)
        i += 1
    return out_data


accounts = {
           "patjcolon": "pass123",
           "lolyngee": "1224"
           }

def login_authenticator(function):
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