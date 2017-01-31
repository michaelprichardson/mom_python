# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:33:30 2017

@author: mrichardson
"""

import numpy as np

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.Values = np.array([x, y])

    def printPoint(self):
        return "Point(%f,%f)"%(self.Values[0], self.Values[1]) 

    def printComplexPoint(self):
        return "Point(%f %fj, %f %fj)"%(self.Values[0].real, self.Values[0].imag, self.Values[1].real, self.Values[1].imag)

    def getX(self):
        return self.Values[0]

    def getY(self):
        return self.Values[1]
