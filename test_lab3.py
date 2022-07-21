import pytest

class Calculator:
    def add(self, a, b):
        return a + b

def test1_add():
    calc = Calculator()
    assert calc.add(1, 1) == 2
    print(calc.add(1,1))
    
def test2_add():
    calc = Calculator()
    assert calc.add(1,2.5) == 3.5
    print(calc.add(1,2.5))
    
def test3_add():
    calc = Calculator()
    assert calc.add(0,0) == 0
    print(calc.add(0,0))
    
def test4_add():
    calc = Calculator()
    assert calc.add(-5,-6)== 11
    print(calc.add(-5,-6))




#print(calc.add(1, 1))