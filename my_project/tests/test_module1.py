# -*- coding: utf-8 -*-

import pytest
from my_project.package1.module1 import fib

from unittest import TestCase

__author__ = "<author>"
__copyright__ = "<author>"
__license__ = "mit"


class TestFib(TestCase):
    def test_fib(self):
        print("Running tests in test_fib:") 
        print(f"\tfib(1) == {fib(1)}")
        self.assertTrue(fib(1) == 1)
        
        print(f"\tfib(2) == {fib(2)}")
        self.assertTrue(fib(2) == 1)
        
        print(f"\tfib(1) == {fib(7)}")
        self.assertTrue(fib(7) == 13)