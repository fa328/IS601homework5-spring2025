'''calculator.py'''
def add(a: float, b: float) -> float:
    '''add function'''
    return a + b

def subtract(a: float, b: float) -> float:
    '''subtract function'''
    return a - b

def multiply(a: float, b: float) -> float:
    '''multiply fuction'''
    return a * b

def divide(a: float, b: float) -> float:
    '''divide function'''
    if b == 0:
        return "Error: Division by zero"
    return a / b
