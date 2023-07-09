from getpass import getpass

# testing out account authentication
# can use a context manager for pulling accounts dict
accounts = {
           "patjcolon": "pass123",
           "lolyngee": "1224"
           }

def authenticator(function):
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


@authenticator
def main():
    print("Access granted! Inner function passed.")


main()