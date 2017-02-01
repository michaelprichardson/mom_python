# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:43:05 2017

@author: michael
"""

import parameters as params
import numpy as np
from scipy import special
import gaussian_quadrature as gq


def fill_z_mat(node_coords, num_elem, elem_nodes, n_gaus=params.gaus_default):
        
    z = np.zeros((num_elem, num_elem), dtype=complex)
    gaus = gq.getGaussianQuadrature(n_gaus)
    
    print(gaus)
            
    for m in range(0, num_elem):
        
        xm = (node_coords[elem_nodes[m][0]][0] + node_coords[elem_nodes[m][1]][0])/2
        ym = (node_coords[elem_nodes[m][0]][1] + node_coords[elem_nodes[m][1]][1])/2
        
        for n in range(0, num_elem):
                
            if m == n:
                wm = np.sqrt( np.power((node_coords[elem_nodes[m][0]][0] - node_coords[elem_nodes[m][1]][0]), 2) + np.power((node_coords[elem_nodes[m][0]][1] + node_coords[elem_nodes[m][1]][1]), 2) )
                z[m][n] = ( params.k0*params.eta0*(wm)/4 )*( 1 - (1j*2/params.pi)*(np.log(params.gam*params.k0*wm/4) - 1 ) )
            else:
                xn = ((node_coords[elem_nodes[n][0]][0]) + (node_coords[elem_nodes[n][1]][0]))/2
                yn = ((node_coords[elem_nodes[n][0]][1]) + (node_coords[elem_nodes[n][1]][1]))/2
                        
                r = np.sqrt( np.power((xm - xn), 2) + np.power((ym - yn), 2) )
                xx = params.k0*r
                
                for k in range(0, n_gaus):
                    wn = gaus[k][1]*np.sqrt( np.power((node_coords[elem_nodes[n][0]][0] - node_coords[elem_nodes[n][1]][0]), 2) + np.power((node_coords[elem_nodes[n][0]][1] + node_coords[elem_nodes[n][1]][1]), 2) )
    #                z[m][n] = (params.k0*params.eta0/4)*wn*(np.sqrt(2/(params.pi*xx))*np.exp(-1j*(xx-(params.pi/4))))
                    z[m][n] = (params.k0*params.eta0/4)*wn*special.hankel2(0, xx)
                
    return -z
    
def create_e_inc(node_coords, num_elem, elem_nodes):
    
    b_vec = np.zeros((num_elem, 1), dtype=complex)
    
    for m in range(0, num_elem):
        x = (node_coords[elem_nodes[m][0]][0] + node_coords[elem_nodes[m][1]][0])/2
        y = (node_coords[elem_nodes[m][0]][1] + node_coords[elem_nodes[m][1]][1])/2
        b_vec[m][0] = np.exp(1j*params.k0*(x*np.cos(params.phi_inc) + y*np.sin(params.phi_inc)))
        
    return b_vec.reshape(num_elem, 1)
    
def calculate_scat(curr, node_coords, num_elem, elem_nodes):
    
    e_scat = np.zeros((params.num_fieldpoints, 1), dtype=complex)
    
    for obs in range(0, params.num_fieldpoints):
        
        x_obs = params.rad_fieldpoints*np.cos(params.phi_fieldpoints[obs])
        y_obs = params.rad_fieldpoints*np.sin(params.phi_fieldpoints[obs])
        
        for n in range(0, num_elem):
            
            xn = (node_coords[elem_nodes[n][0]][0] + node_coords[elem_nodes[n][1]][0])/2
            yn = (node_coords[elem_nodes[n][0]][1] + node_coords[elem_nodes[n][1]][1])/2
            
            r = np.sqrt( np.power((x_obs - xn), 2) + np.power((y_obs - yn), 2) )
            xx = params.k0*r
            
            wn = np.sqrt( np.power((node_coords[elem_nodes[n][0]][0] - node_coords[elem_nodes[n][1]][0]), 2) + np.power((node_coords[elem_nodes[n][0]][1] + node_coords[elem_nodes[n][1]][1]), 2) )
#            z = (params.k0*params.eta0/4)*wn*(np.sqrt(2/(params.pi*xx))*np.exp(-1j*(xx-(params.pi/4))))
            z = (params.k0*params.eta0/4)*wn*special.hankel2(0, xx)
            
            e_scat[obs][0] = e_scat[obs][0] + z*curr[n][0]
                
    return e_scat
    
def calculate_mom_different_quads(node_coords, num_elem, elem_nodes):
    
    quads = params.gaus_quads
    
    for ii in range(0, len(quads)):
        print(ii)