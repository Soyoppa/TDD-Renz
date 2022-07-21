import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
        

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

    
def test1_subtract(base_calculator):
    assert Calculator.subtract(base_calculator.name,1,1) == 0
    
def test2_subtract(base_calculator):
    assert Calculator.subtract(base_calculator.name,-1,1) == -2

def test3_subtract(base_calculator):
    assert Calculator.subtract(base_calculator.name,-1,-1) == 0
    
def test4_subtract(base_calculator):
    assert Calculator.subtract(base_calculator.name,1,-1) == 2
    

def test1_multiply(base_calculator):
    assert Calculator.multiply(base_calculator.name,1,1) == 1
    
def test2_multiply(base_calculator):
    assert Calculator.multiply(base_calculator.name,1,-1) == -1
    
def test3_multiply(base_calculator):
    assert Calculator.multiply(base_calculator.name,-1,1) == -1
    
def test4_multiply(base_calculator):
    assert Calculator.multiply(base_calculator.name,-1,-1) ==1
    
def test5_multiply(base_calculator):
    assert Calculator.multiply(base_calculator.name,1, 2) == 2
    