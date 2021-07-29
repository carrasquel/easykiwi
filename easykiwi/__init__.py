"""
Queue Messaging Application with Python
==================================
Easykiwi is a Framework for Queue Messaging Application
Development for Python and RabbitMQ.

It aims to provide simple and efficient solutions
to the most common messaging techniques.
"""

__version__ = '1.1'

from .core import Kiwi
from .client import KiwiClient
from .cli import kiwi_cli as cli
