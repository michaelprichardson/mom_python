# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:22:29 2017

@author: michael
"""

import parameters as params
import numpy as np
import create_mesh as mesh
import mom_functions as mom
import plot
import time

mesh_functions = [mesh.create_line(), mesh.create_reflector()]

def run_mom_on_model(num_model):

    s = time.time()
    
    # Generate mesh
    start = time.time()
    msh = mesh_functions[num_model]
    
    print("Generating mesh took {:.2f}s".format(time.time() - start))
    
    node_coords = msh['node_coords']
    num_elem = msh['num_elem']
    elem_nodes = msh['elem_nodes']
    
    # Calculate A matrix and b vector
    start = time.time()
    A_mat = mom.fill_z_mat(node_coords, num_elem-1, elem_nodes)
    b_vec = mom.create_e_inc(node_coords, num_elem-1, elem_nodes)
    
    print("Filling matrices took {:.2f}s".format(time.time() - start))
    
    # Calculate current vector
    curr = np.dot(np.linalg.inv(A_mat), b_vec)
    
    # Calculate scatter field and convert to dB
    start = time.time()
    scat = mom.calculate_scat(curr, node_coords, num_elem-1, elem_nodes)
    scat = mom.calculate_db_scat(scat)
    
    print("Scatter calculation took {:.2f}s".format(time.time() - start))
    
    # Plot mesh
    plot.plot_mesh(node_coords)
    
    # Plot real scatter field
    plot.plot_scatter(scat)
    plot.plot_scat_polar(scat)
    
    print("Finished MoM calculation in {:.2f}s".format(time.time() - s))
    
def run_mom_multiple_gaus_quads(num_model):    

    # Generate mesh
    msh = mesh_functions[num_model]
        
    node_coords = msh['node_coords']
    num_elem = msh['num_elem']
    elem_nodes = msh['elem_nodes']
    
    data = mom.calculate_mom_different_quads(node_coords, num_elem-1, elem_nodes)
        
    plot.plot_multiple_plots(data)
    
run_mom_on_model(0)

#run_mom_multiple_gaus_quads(0)