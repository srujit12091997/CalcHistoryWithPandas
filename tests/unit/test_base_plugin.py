# test_base_plugin.py
from app.plugins.base_plugin import BasePlugin

def test_base_plugin_initialize():
    base_plugin = BasePlugin()
    assert base_plugin is not None  # Check if BasePlugin object is created successfully

