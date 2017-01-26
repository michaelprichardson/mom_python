# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:33:30 2017

@author: mrichardson
"""

import math

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def printPoint(self):
        return "Point(%f,%f)"%(self.X, self.Y) 

    def printComplexPoint(self):
        return "Point(%f %fj,%f %fj)"%(self.X.real, self.X.imag, self.Y.real, self.Y.imag)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y
