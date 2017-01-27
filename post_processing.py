# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:38:52 2017

@author: michael
"""

import numpy as np
import cmath
import math
import parameters as params

def pointsInCircum(r, n=100):
    return [(math.cos(2*math.pi/n*x)*r, math.sin(2*math.pi/n*x)*r) for x in xrange(0, n+1)]
    
def calculateFarFields(current, segs, in_db):
    obs_points = pointsInCircum(params.PHI_RADIUS, int(params.PHI_END/params.PHI_INCREMENT))
    
    e_constant = params.K_0*params.ETA_0/4
    e_scat = np.zeros((len(obs_points), 1), dtype=np.complex)
    
    for ii in range(0, len(obs_points)):
        temp_e_scat = 0
        
        for jj in range(0, len(current)):
            
            # Add Gaussian Quadrature here?
            
            R = np.sqrt((np.power((obs_points[ii][0] - segs[jj].getCenter().getX()), 2) + 
                            np.power((obs_points[ii][1] - segs[jj].getCenter().getY()), 2)))
                        
            curr = current[jj][0] + current[jj][1]
            
            x = params.K_0*R
            
            seg_width = segs[jj].getSegmentLength()
            
            scat = curr*e_constant*seg_width*np.sqrt(params.PI/(2*x))*np.exp(-1j*x) 
            
            temp_e_scat = temp_e_scat + (scat)
    
        if in_db:
            e_scat[ii][0] = 20*np.log(cmath.sqrt(2*params.PI*np.abs(temp_e_scat)))
        else:
            e_scat[ii][0] = np.abs(temp_e_scat)
    
    return e_scat