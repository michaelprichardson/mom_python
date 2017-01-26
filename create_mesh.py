# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:53:38 2017

@author: mrichardson
"""

import parameters as params
import point
import segment
import math

def create_line():
    side_length = 20*params.LAM_0
        
    m_length = params.MAX_MESH_SIZE
    mesh = []
    
    n_segs = int(side_length/m_length)

    for ii in range(0, n_segs/2):
        if ii == 0:
            p_start = point.Point(0.0, 0.0)
            n_start = point.Point(0.0, 0.0)
        else:
            start_val = ii*m_length
            p_start = point.Point(0.0, start_val)
            n_start = point.Point(0.0, -start_val)
            
        next_val = (ii+1)*m_length
        p_end = point.Point(0.0, next_val)
        n_end = point.Point(0.0, -next_val)
        
        p_seg = segment.Segment(p_start, p_end)
        n_seg = segment.Segment(n_start, n_end)
        
        mesh.append(p_seg)
        mesh.append(n_seg)
        
    return mesh

def create_reflector():
    side_length = 10*params.LAM_0
    m_length = params.MAX_MESH_SIZE
    n_segs = int(side_length/m_length)
    
    mesh = []
       
    for ii in range(0, n_segs):
        if ii == 0:
            p_start = point.Point(0.0, 0.0)
            n_start = point.Point(0.0, 0.0)
        else:
            start_val = ii*m_length
            p_start = point.Point(start_val, start_val)
            n_start = point.Point(start_val, -start_val)
            
        next_val = (ii+1)*m_length
        p_end = point.Point(next_val, next_val)
        n_end = point.Point(next_val, -next_val)
        
        p_seg = segment.Segment(p_start, p_end)
        n_seg = segment.Segment(n_start, n_end)
        
        mesh.append(p_seg)
        mesh.append(n_seg)
    
    return mesh
    
def create_circle():
    radius = 10*params.LAM_0
    circum = 2*params.PI*radius
    m_length = params.MAX_MESH_SIZE
    n_segs = int(circum/m_length)
    ang_inc = 2*params.PI/n_segs
    
    mesh = []
       
    for ii in range(0, n_segs):
        if ii == 0:
            start = point.Point(radius, 0.0)
        else:
            start_ang = ii*ang_inc
            start = point.Point(radius*math.cos(start_ang), radius*math.sin(start_ang))
            
        next_ang = (ii+1)*ang_inc
        end = point.Point(radius*math.cos(next_ang), radius*math.sin(next_ang))
        
        seg = segment.Segment(start, end)
        
        mesh.append(seg)
    
    return mesh

def create_line_with_angled_edge():
    side_length = 10*params.LAM_0
    ang_length = 5*params.LAM_0
    obs_length = 8*params.LAM_0
    dist_away = 4*params.LAM_0
    shift_obs = 1*params.LAM_0
    
    m_length = params.MAX_MESH_SIZE
    mesh = []
    
    n_segs = int(side_length/m_length)

    for ii in range(0, n_segs/2):
        if ii == 0:
            p_start = point.Point(0.0, 0.0)
            n_start = point.Point(0.0, 0.0)
        else:
            start_val = ii*m_length
            p_start = point.Point(0.0, start_val)
            n_start = point.Point(0.0, -start_val)
            
        next_val = (ii+1)*m_length
        p_end = point.Point(0.0, next_val)
        n_end = point.Point(0.0, -next_val)
        
        p_seg = segment.Segment(p_start, p_end)
        n_seg = segment.Segment(n_start, n_end)
        
        mesh.append(p_seg)
        mesh.append(n_seg)
        
    n_segs = int(ang_length/m_length)
    
    for ii in range(0, n_segs):
        if ii == 0:
            start = point.Point(0.0, ang_length)
        else:
            start_val = ii*m_length
            start = point.Point(start_val, start_val + ang_length)
            
        next_val = (ii+1)*m_length
        end = point.Point(next_val, next_val + ang_length)
        
        seg = segment.Segment(start, end)
        
        mesh.append(seg)
        
    n_segs = int(obs_length/m_length)
    
    for ii in range(0, n_segs/2):
        if ii == 0:
            p_start = point.Point(dist_away, 0.0 + shift_obs)
            n_start = point.Point(dist_away, 0.0 + shift_obs)
        else:
            start_val = ii*m_length
            p_start = point.Point(dist_away, start_val + shift_obs)
            n_start = point.Point(dist_away, -start_val + shift_obs)
            
        next_val = (ii+1)*m_length
        p_end = point.Point(dist_away, next_val + shift_obs)
        n_end = point.Point(dist_away, -next_val + shift_obs)
        
        p_seg = segment.Segment(p_start, p_end)
        n_seg = segment.Segment(n_start, n_end)
        
        mesh.append(p_seg)
        mesh.append(n_seg)
        
    return mesh
    