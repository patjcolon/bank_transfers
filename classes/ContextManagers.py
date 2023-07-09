""""""

import json
#from helper_functions.typr import typr


class File:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(f"Connecting to database {self.name}...")

        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from database {self.name}...")

    
    def read_file(self):
        try:
            print("trying...")
            with open(self.name, "r") as databases:
                database = json.load(databases)
                yield database
        except FileNotFoundError:
            print("except!")
        finally:
            print("finally")


# when i come back: ... <3
with File("test.json") as file:
    print(file.read_file())
    db_gen = file.read_file()
    for i in db_gen:
        print("iterating!")
        print(i)
        db = i
        print(db)
    print("huh")
