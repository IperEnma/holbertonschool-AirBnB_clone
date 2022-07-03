#!/usr/bin/python3
"""
testing class console
"""

import pep8
import console
from console import HBNBCommand
from unittest import TestCase
import unittest
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """class for testing class console"""

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(console.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_pep8(self):
        """ check pep8 style """
        style = pep8.StyleGuide()
        filenames = ["console.py", "tests/test_console.py"]
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0)

    def test_attr_doc(self):
        """ check methods and doc """
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertTrue(hasattr(HBNBCommand, "do_count"))
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_console(self):
        """ check console """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")

if __name__ == '__main__':
    unittest.main()
