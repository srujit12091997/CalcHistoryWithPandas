# command_interface.py

class CommandInterface:
    """Interface for command execution."""
    def execute_command(self, calculator, *args):
        """Execute a command."""
        raise NotImplementedError("Subclasses must implement execute_command method")
