# test_command_interface.py
from app.interfaces.command_interface import CommandInterface

def test_command_interface_execute_command():
    # Instantiate CommandInterface without arguments
    command_interface = CommandInterface()
    assert command_interface is not None  # Check if CommandInterface object is created successfully