""" context manager, idea was to use it for storing and updating bank account info
and another idea to try to make individual user transfer requests 
might come back to some day
by patjcolon 
last updated 7/9/2023"""

import json
#from helper_functions.typr import typr


class File:
    """ custom context manager class for making file generators
    closes out file when done"""
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(f"Connecting to database {self.name}...")

        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from database {self.name}...")

    
    def read_file(self):
        """yields file generator to save on resources and close out actual file"""
        try:
            print("trying...")
            with open(self.name, "r") as databases:
                database = json.load(databases)
                yield database
        except FileNotFoundError:
            print("except!")
        finally:
            print("finally")


# learning how generators work
"""
with File("test.json") as file:
    print(file.read_file())
    db_gen = file.read_file()
    for i in db_gen:
        print("iterating!")
        print(i)
        db = i
        print(db)
    print("huh")
"""