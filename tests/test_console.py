#!/usr/bin/python3
"""
Console Unit tests
"""
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage


class Test_console_prompt(unittest.TestCase):
