# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6, 7, 9),
                         'Scalene', '6,7,9 should be scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(7, 7, 9),
                         'Isosceles', '7,7,9 should be isoceles')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 9),
                         'NotATriangle', '3,3,9 should be not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(3, 3, -3),
                         'InvalidInput', '3,3,-3 should be invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201, 201, 201),
                         'InvalidInput', '201,201,201 should be invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(3, "hello", 11),
                         'InvalidInput', '3,"hello",11 should be invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
