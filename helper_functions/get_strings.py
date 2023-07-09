""""""

import string
from functools import wraps
from .typr import typr


def get_strings(input_type: str):
    """ Decorator factory, input_type is used as key in a decorator selection dictionary
    'name' : decorator_get_name(function) - returns str that is valid and formatted as a name"""
    
    #
    def retry_entry(failed_attempts):
        max_attempts = 5
        remaining_attempts = max_attempts - failed_attempts
        if failed_attempts == 0:
            return
        if remaining_attempts == 0:
            typr("\nToo many failed attempts. ", "fast", False)
            return False
        if remaining_attempts == 1:
            typr("\nFinal attempt. ", "fast", False)
            typr("Retry: ", "fast", False)
            return
        typr(f"\n{max_attempts - failed_attempts} attempts remaining. ", "fast", False)
        typr("Retry: ", "fast", False)
        return

    def decorator_get_name(function):
        """ gets input() for name and returns a formatted valid name, repeating input until validated.
        Formatting: '   tim   guy ' -> 'Tim Guy'
        Validates string is within min and max length, and only uses letters or spaces.
        only counts spaces that are not leading or trailing,
        and only counts 1 spaces per 1+ spaces in between words"""
        
        @wraps(function)    
        def wrapper_get_name(self, name: str = None):
            # admin use only: if name is given in wrapped_func(name), it will auto pass name.
            if name is not None:
                return function(self, name)
            """"""
            # needs documentation string.
            
            # setting min and max length for name
            min_name_length = 5
            max_name_length = 16

            # formatting and validation loop. formatting: '   tim   guy ' -> 'Tim Guy'
            name_valid = False
            failed_attempts = 0
            while not name_valid:
                if retry_entry(failed_attempts) is False:
                    return function(self, None)

                name = input()
                # formatting, removing whitespace except 1 ' ' between words and capitalizing first letters
                name = ' '.join(name.split())
                name = name.title()
                
                # checking name is within character length requirements
                if len(name) < min_name_length or len(name) > max_name_length:
                    typr(f"{name} is not a valid name.",
                        f"Names must be between {min_name_length} and {max_name_length} characters long.")
                    failed_attempts += 1
                    continue
                for character in name:
                    # checking if name contains any characters other than letters and spaces
                    if character not in string.ascii_letters and character != " ":
                        failed_attempts += 1
                        name_valid = False
                        typr(f"{name} is not a valid name.",
                            "Names may only contain upper and lowercase letters.")
                        break
                    # if each char is valid this gets passed; breaks outer while input loop
                    name_valid = True
            # giving the wrapped function the valid, formatted name as argument
            return function(self, name)
        return wrapper_get_name
    

    def decorator_get_pin(function):
        """"""
        # needs documentation string. validates input returns int between range
        @wraps(function)
        def wrapper_get_pin(self, pin: str = None):
            # admin use only: if pin is given in wrapped_func(pin), it will auto pass pin.
            if pin is not None:
                return function(self, pin)

            # setting min and max length for pin
            min_pin_length = 4
            max_pin_length = 6

            # validation loop
            pin_valid = False
            failed_attempts = 0
            while not pin_valid:
                if retry_entry(failed_attempts) is False:
                    return function(self, None)

                pin = input()
                pin_length = len(pin)
                if not min_pin_length <= pin_length <= max_pin_length:
                    typr("PIN must be a 4 to 6 digits long.")
                    failed_attempts += 1
                    continue
                
                for digit in pin:
                    if digit not in string.digits:
                        pin_valid = False
                        typr(f"{pin} is not a valid PIN.")
                        typr("PIN must be a 4 to 6 digits long positive whole number.")
                        failed_attempts += 1
                        break
                    pin_valid = True
            # giving the wrapped function the valid PIN
            return function(self, pin)
        
        # calling wrapper_get_pin which gives the decorated function a valid pin as an argument
        return wrapper_get_pin

    
    def decorator_get_password(function):
        """"""
        @wraps(function)
        def wrapper_get_password(self, password: str = None):
            #
            if password is not None:
                return function(self, password)
            #
            password_valid = False
            while not password_valid:
                password = input()

        return wrapper_get_password

    
    # dictionary of functions to call that use input_type as key
    input_type_choices = {
                         "name": decorator_get_name,
                         "pin": decorator_get_pin,
                         "password": decorator_get_password
    }

    return input_type_choices[input_type]