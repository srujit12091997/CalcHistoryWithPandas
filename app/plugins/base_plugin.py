# base_plugin.py

class BasePlugin:
    """Base class for plugins."""
    def execute(self):
        """Execute plugin functionality."""
        raise NotImplementedError("Subclasses must implement execute method")
