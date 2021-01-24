import unittest
from io import StringIO
import sys


def foo():
    print("foo")


def test_foo():
    out = StringIO()
    # sys.stdout = out
    foo()
    sys.stdout = sys.__stdout__
    # assert out.getvalue() is "foo"


class TestLinkedList(unittest.TestCase):

    def test(self):
        self.assertEquals(1,2)
        print("test")

    def test_print(self):
        capturedOutput = StringIO()
        # sys.stdout = capturedOutput
        test_list = [5, 1, 13, 7]
        print(test_list)
        # sys.stdout = sys.__stdout__

        print('Captured ', capturedOutput.getvalue())
        # self.assertEqual(1, 1)
