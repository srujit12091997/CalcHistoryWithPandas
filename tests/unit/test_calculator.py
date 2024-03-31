# tests/unit/test_calculator.py

import os
import pandas as pd
import pytest
from app.core.calculator import Calculator,CalculatorError

def test_calculator_add():
    calculator = Calculator()
    calculator.set_strategy(calculator.AddStrategy())
    assert calculator.calculate(4, 5) == 9

def test_calculator_subtract():
    calculator = Calculator()
    calculator.set_strategy(calculator.SubtractStrategy())
    assert calculator.calculate(9, 3) == 6

def test_calculator_multiply():
    calculator = Calculator()
    calculator.set_strategy(calculator.MultiplyStrategy())
    assert calculator.calculate(2, 3) == 6

def test_calculator_divide():
    calculator = Calculator()
    calculator.set_strategy(calculator.DivideStrategy())
    assert calculator.calculate(6, 2) == 3


def test_calculator_divide_by_zero():
    calculator = Calculator()
    calculator.set_strategy(calculator.DivideStrategy())
    with pytest.raises(CalculatorError):
        calculator.calculate(6, 0)


def test_calculator_update_history_save():
    calculator = Calculator()
    calculator.update_history(3, 4, 'Subtract', -1)
    calculator.update_history(2, 7, 'Multiply', 14)
    calculator.update_history(8, 2, 'Divide', 4)
    calculator.clear_history()
    calculator.update_history(5, 5, 'Add', 10)
    assert os.path.exists(calculator.history_file)
    assert os.path.getsize(calculator.history_file) > 0
    history_df = pd.read_csv(calculator.history_file)
    assert history_df.shape[0] == 1
    assert history_df.iloc[0]['Operand A'] == 5
    assert history_df.iloc[0]['Operand B'] == 5
    assert history_df.iloc[0]['Operation'] == 'Add'
    assert history_df.iloc[0]['Result'] == 10


def test_calculator_update_history():
    calculator = Calculator()
    calculator.update_history(5, 6, 'Add', 11)
    assert calculator.history_df.shape[0] == 2  # Corrected assertion to reflect the updated behavior


def test_calculator_clear_history():
    calculator = Calculator()
    calculator.update_history(3, 4, 'Subtract', -1)
    calculator.update_history(2, 7, 'Multiply', 14)
    calculator.update_history(8, 2, 'Divide', 4)
    calculator.clear_history()
    assert calculator.history_df.empty  # Asserting that the history DataFrame is empty
    assert not os.path.exists(calculator.history_file) 



