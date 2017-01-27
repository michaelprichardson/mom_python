# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:50:34 2017

@author: mrichardson
"""

import parameters as params
import math
import numpy as np
import point
from scipy import special
import post_processing as pp

def calculate_mom(segs):
    centers = calculate_seg_centers(segs)
    
    b_vec = fill_b_matrix(centers)
    A_mat = fill_z_matrix(centers, segs)   
    J_MoM = A_mat/b_vec
    
    scat = calculate_e_scat(J_MoM, segs)
       
    return scat
    
def calculate_seg_centers(segs):
    centers = np.empty((len(segs),2))
    
    for ii in range(0, len(segs)):
        centers[ii][0] = segs[ii].getCenter().getX()
        centers[ii][1] = segs[ii].getCenter().getY()
        
    return centers
    
def fill_b_matrix(centers):
    num_elem = len(centers)
    b_vec = np.zeros((num_elem, 1), dtype=complex)
    
    inc_ang = math.radians(params.INCIDENT_ANGLE)
    
    for ii in range(0, num_elem):
        x = centers[ii][0]
        y = centers[ii][1]
        b_vec[ii][0] = np.exp(-1j*params.K_0*(-x*np.cos(inc_ang) - y*np.sin(inc_ang)))

    return b_vec
    
def fill_z_matrix(centers, segs):
    num_elem = len(centers)
    z = np.zeros((num_elem, num_elem), dtype=complex)
    
    for m in range(0, num_elem):
        
        xm = centers[m][0]
        ym = centers[m][1]
    
        for n in range(0, num_elem):
            
            xn = centers[n][0]
            yn = centers[n][1]
            
            R = np.sqrt( np.power((xm-xn), 2) + np.power((ym-yn), 2) )
            x = params.K_0*R
            
            if m == n:
                wm = segs[m].getSegmentLength()
                z[m][n] = (params.K_0*params.ETA_0*wm/4)*(1 - (1j*2/params.PI)*(np.log(params.GAM_0*params.K_0*wm/4) - 1 ))
            else:
                wn = np.sqrt( np.power(xm - xn, 2) + np.power(ym - yn, 2) )
                z[m][n] = (params.K_0*params.ETA_0/4)*wn*special.hankel2(0, x)
                
    
    return -z

    
def calculate_e_scat(curr, segs):
    
    obs_points = pp.pointsInCircum(params.PHI_RADIUS, int(params.PHI_END/params.PHI_INCREMENT))
       
#    seg_centers = get_seg_centers(segs)
#    element_width = get_seg_widths(segs)
    
    num_fps = len(obs_points)
    num_elem = len(segs)
    
    fp_ez_data = np.zeros((num_fps, 1), dtype=complex)

    for k in range(0, num_fps):
    
        xm = obs_points[k][0]
        ym = obs_points[k][1]
        
        for m in range(0, num_elem):
            
            xn = segs[m].getCenter().getX()
            yn = segs[m].getCenter().getX()

            R = np.sqrt( np.power((xm-xn), 2) + np.power((ym-yn), 2) )
            x = params.K_0*R
        
            wn = np.sqrt( np.power(xm - xn, 2) + np.power(ym - yn, 2) )
            z = (params.K_0*params.ETA_0/4)*wn*special.hankel2(0, x)
                
            for n in range(0, num_elem):

                fp_ez_data[k][0] = fp_ez_data[k][0] + z*curr[m][n]
                           
    return fp_ez_data
    
def get_seg_centers(segs):
    centers = np.zeros((len(segs), 2))
    
    for ii in range(0, len(segs)):
        tmp = segs[ii].getCenter()
        centers[ii][0] = tmp.getX()
        centers[ii][1] = tmp.getY()
        
    return centers
    
def get_seg_widths(segs):
    wids = np.zeros((len(segs), 1))
    
    for ii in range(0, len(segs)):
        wids[ii][0] = segs[ii].getSegmentLength()
        
    return wids
    
def get_seg_x1(segs):
    x1 = np.zeros((len(segs), 1))
    
    for ii in range(0, len(segs)):
        x1[ii][0] = segs[ii].getStart().getX()
        
    return x1
    
def get_seg_x2(segs):
    x2 = np.zeros((len(segs), 1))
    
    for ii in range(0, len(segs)):
        x2[ii][0] = segs[ii].getEnd().getX()
        
    return x2
    
def get_seg_y1(segs):
    y1 = np.zeros((len(segs), 1))
    
    for ii in range(0, len(segs)):
        y1[ii][0] = segs[ii].getStart().getY()
        
    return y1
    
def get_seg_y2(segs):
    y2 = np.zeros((len(segs), 1))
    
    for ii in range(0, len(segs)):
        y2[ii][0] = segs[ii].getEnd().getY()
        
    return y2
    