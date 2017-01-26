# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:23:40 2017

@author: mrichardson
"""

import argparse
import point
import segment
import create_mesh as mesh
import plot
import test_2d_mrpo_ipo as test
import shadowing
import current_calculation as cc
import post_processing as pp
import useful_functions as uf
import calculate_mom_data as mom

#test.runTests()

#parser = argparse.ArgumentParser()
#
#parser.add_argument("model_name", type=int, choices=[0, 1, 2], help="The name of the model to be simulated")
#parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
#                    help="Increase output verbosity")
#                    
#args = parser.parse_args()

# Build geometry and mesh
geometry = [mesh.create_line(), mesh.create_reflector(), mesh.create_circle(), mesh.create_line_with_angled_edge()]

#msh = geometry[args.model_name]
msh = geometry[0]
#plot.plot_mesh(msh)
#
#msh_norms = shadowing.calculate_segment_normals(msh)
#uf.print_message('There are {} segments'.format(len(msh)))
#
## Calculate the shadowing for the geometry
#init_vis = shadowing.calculate_initial_plane_wave_shadowing(msh, msh_norms)
#vis = shadowing.calculate_segment_shadowing(msh, msh_norms)
#uf.print_message('Finished determining the shadowing')
#
## Calculate the currents for each method
#mrpo_current = cc.calculate_mrpo_currents(init_vis, vis, msh, msh_norms)
#uf.print_message('Finished calculating the current')
#
## Calculate the far field and RCS for each method
#data = pp.calculateFarFields(mrpo_current, msh, True)
#uf.print_message('Finished calculating the post processing')
#
## Plot all the relavent information - Geometry, Far field, RCS, iteration history 
## and convergence history for the iterative methods
##plot.plot_mesh(msh)
#plot.plot_data(data)


data = mom.calculate_mom(msh)

plot.plot_data(data)