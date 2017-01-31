# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:33:31 2017

@author: mrichardson
"""

import math
from point import Point
import numpy as np
import useful_functions as uf

class Segment(object):
    '''Creates a segment on a coordinate plane with values start and end points.'''

    def __init__(self, start, end):
        '''Defines start and end co-ordinates'''
        self.Start = start
        self.End = end

    def printSegment(self):
        return "Segment(%s,%s)"%(self.Start.printPoint(), self.End.printPoint()) 

    def getStart(self):
        return self.Start

    def getEnd(self):
        return self.End
        
    def getCenter(self):
        x = (self.Start.getX() + self.End.getX())/2
        y = (self.Start.getY() + self.End.getY())/2
        return Point(x, y)
        
    def getSegmentLength(self):
        return math.sqrt((self.Start.getX() - self.End.getX())**2 + (self.Start.getY() - self.End.getY())**2)
        
    def getSegmentNormals(self):
        normals = []
        
        dx = self.End.getX() - self.Start.getX()
        dy = self.End.getY() - self.Start.getY()
        
        norm = math.sqrt((dx**2 + dy**2));
        
        x = abs(dx/norm);
        y = abs(dy/norm);
        
        normals.append(Point(-y, x))
        normals.append(Point(y, -x))
        
        return normals

    def contains_point(self, pnt):
        seg_len = self.getSegmentLength()
        seg_start_pnt_len = uf.calculateDistance(self.Start, pnt)
        seg_end_pnt_len = uf.calculateDistance(self.End, pnt)
        
        if uf.isZero((seg_len - (seg_start_pnt_len + seg_end_pnt_len))) == 0:
            return True
            
        return False