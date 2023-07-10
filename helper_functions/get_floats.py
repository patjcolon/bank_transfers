"""Really only gets a cash value float. makes sure input is an actual cash value (see below)
is a wrapper that injects cash float into wrapped function's first parameter (not self)
by patjcolon
Last updated: 7/9/2023"""



from math import floor
from functools import wraps
from .typr import typr, get_user_input

def get_cash_amount(function):
        """gets a cash value from input and validates it
        gets a float and ensures it is at least 0.01 and doesnt include fractions smaller than that"""
        @wraps(function)
        def wrapper_get_cash_amount(self, cash_amount: str = None):
            # admin use only: if cash_amount is given in wrapped_func(cash_amount), it will auto pass cash_amount.
            if cash_amount is not None:
                return function(self, cash_amount)

            cash_input = get_user_input().split(",")
            cash_input = ''.join(cash_input)
            try:
                cash_input = float(cash_input)
                cash_amount = floor(cash_input * 100 + 0.00001)/100.0
                if cash_input != cash_amount:
                    typr("Amount cannot include fractions of a penny.")
                    return function(self, None)
                if cash_amount < 0.01:
                    typr("Amount must be at least 1 penny.")
                    return function(self, None)
                else: 
                    return function(self, cash_amount)
            except ValueError:
                typr(f"{cash_input} is not a valid cash value.")
                return function(self, None)
        
        # calling wrapper_get_cash_amount which gives the decorated function a valid cash_amount as an argument
        return wrapper_get_cash_amount



