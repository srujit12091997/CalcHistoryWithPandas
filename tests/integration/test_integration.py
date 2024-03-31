# tests/integration/test_integration.py

import pytest
from app.core.calculator import Calculator, AddStrategy, DivideStrategy, CalculatorError  # Import CalculatorError

# Integration tests for Calculator class

def test_calculator_integration():
    calculator = Calculator()
    calculator.set_strategy(calculator.AddStrategy())
    assert calculator.calculate(4, 5) == 9
    calculator.set_strategy(calculator.SubtractStrategy())
    assert calculator.calculate(9, 3) == 6
    calculator.set_strategy(calculator.MultiplyStrategy())
    assert calculator.calculate(2, 3) == 6
    calculator.set_strategy(calculator.DivideStrategy())
    assert calculator.calculate(6, 2) == 3

def test_calculator_integration_divide_by_zero():
    calculator = Calculator()
    calculator.set_strategy(calculator.DivideStrategy())
    with pytest.raises(CalculatorError):  # Use CalculatorError directly
        calculator.calculate(6, 0)
