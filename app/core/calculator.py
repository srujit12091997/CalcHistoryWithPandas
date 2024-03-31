import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)

class CalculatorError(Exception):
    """Custom exception class for Calculator errors"""
    pass

class AddStrategy:
    """Strategy class for addition operation."""
    def calculate(self, a, b):
        return a + b

class SubtractStrategy:
    """Strategy class for subtraction operation."""
    def calculate(self, a, b):
        return a - b

class MultiplyStrategy:
    """Strategy class for multiplication operation."""
    def calculate(self, a, b):
        return a * b

class DivideStrategy:
    """Strategy class for division operation."""
    def calculate(self, a, b):
        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a / b

class Calculator:
    AddStrategy = AddStrategy  # Assign AddStrategy to Calculator class attribute
    SubtractStrategy = SubtractStrategy
    MultiplyStrategy = MultiplyStrategy
    DivideStrategy = DivideStrategy  # Assign DivideStrategy to Calculator class attribute

    def __init__(self, history_file='data/history.csv'):
        self.history_file = history_file
        self.history_df = self.load_history()
        self.strategy = None

    def set_strategy(self, strategy):
        """Set the strategy for calculation."""
        self.strategy = strategy

    def calculate(self, a, b):
        """Calculate using the selected strategy."""
        if self.strategy is None:
            raise CalculatorError("No strategy set")
        return self.strategy.calculate(a, b)

    def load_history(self):
        try:
            df = pd.read_csv(self.history_file)
            if df.empty:
                # If the DataFrame is empty, return an empty DataFrame
                return pd.DataFrame(columns=['Operand A', 'Operand B', 'Operation', 'Result'])
            else:
                return df
        except FileNotFoundError:
            # Return an empty DataFrame if history file does not exist
            return pd.DataFrame(columns=['Operand A', 'Operand B', 'Operation', 'Result'])

    def update_history(self, operand_a, operand_b, operation, result):
        new_entry = pd.DataFrame({
            'Operand A': [operand_a],
            'Operand B': [operand_b],
            'Operation': [operation],
            'Result': [result]
        })
        # Concatenate new entry with the existing DataFrame
        if self.history_df.empty:
            self.history_df = new_entry
        else:
            self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
        # Save the updated DataFrame to CSV
        self.history_df.to_csv(self.history_file, index=False)

    def clear_history(self):
        # Clear the history DataFrame and save to CSV
        self.history_df = pd.DataFrame(columns=['Operand A', 'Operand B', 'Operation', 'Result'])
        self.history_df.to_csv(self.history_file, index=False)
        # Remove the history file if it exists
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
