'''test operations'''
import decimal
from decimal import Decimal
# from typing import Self
import pytest # type: ignore
# from calculator.calculation import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculations:
    '''calculation class'''
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        '''perform function'''
        return self.operation(self.a, self.b)

    def add(self):
        '''Test that addition function works'''
        return add(self.a, self.b)

    def subtract(self):
        '''Test that subtraction function works'''
        return subtract(self.a, self.b)

    def multiply(self):
        '''Test that multiplication function works'''
        return multiply(self.a, self.b)

def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculations(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(decimal.DivisionByZero):
        calculation = Calculations(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
