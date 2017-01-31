# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:27:49 2017

@author: michael
"""

import numpy as np
import parameters as params

length = params.line_length
elem_size = params.meshsize_solve

def create_line():
    num_elem = int(round(length/elem_size))+1
    node_coords = np.zeros((num_elem, 2))
    curr_node = np.array([0, -length/2])
        
    for ii in range(0, num_elem):
        node_coords[ii] = curr_node
        curr_node = np.array([0, curr_node[1] + elem_size])
        
    elem_nodes = np.zeros((num_elem, 2))
    
    for ii in range(0, num_elem):
        elem_nodes[ii] = np.array([ii, ii+1])
    
    return {"num_elem": num_elem, "node_coords": node_coords, "elem_nodes": elem_nodes}
    
def create_reflector():
    num_elem = 2*(int(round(length/elem_size)))
    node_coords = np.zeros((num_elem, 2))
    curr_node = np.array([0, 0])
    
    count = 0
    
    for ii in range(0, int(num_elem/2)):
        node_coords[count] = curr_node
        curr_node = np.array([(ii+1)*elem_size, (ii+1)*elem_size])
        count = count + 1
    
    curr_node = np.array([0, 0])
        
    for ii in range(0, int(num_elem/2)):
        node_coords[count] = curr_node
        curr_node = np.array([(ii+1)*elem_size, -1*(ii+1)*elem_size])
        count = count + 1
    
    elem_nodes = np.zeros((num_elem, 2))
    
    for ii in range(0, num_elem):
        elem_nodes[ii] = np.array([ii, ii+1])
        
    return {"num_elem": num_elem, "node_coords": node_coords, "elem_nodes": elem_nodes}