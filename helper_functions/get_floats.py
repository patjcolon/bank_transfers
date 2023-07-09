from math import floor
from functools import wraps
from .typr import typr

def get_cash_amount(function):
        """"""
        # needs documentation string. validates input returns int between range
        @wraps(function)
        def wrapper_get_cash_amount(self, cash_amount: str = None):
            # admin use only: if cash_amount is given in wrapped_func(cash_amount), it will auto pass cash_amount.
            if cash_amount is not None:
                return function(self, cash_amount)

            #
            cash_input = input().split(",")
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



