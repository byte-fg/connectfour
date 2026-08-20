"""ConnectFour: A connect four game against a simple AI that blocks threats."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]