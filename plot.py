# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:26:13 2017

@author: mrichardson
"""

import matplotlib.pyplot as plt
import parameters as params
import numpy as np

def plot_mesh(mesh, n=1):
    lam_0 = params.LAM_0
    
    for ii in range(0, len(mesh)):
        s_start = mesh[ii].getStart()
        s_end = mesh[ii].getEnd()
                
        plt.plot([s_start.getX()/lam_0, s_end.getX()/lam_0], [s_start.getY()/lam_0, s_end.getY()/lam_0], '-r')
    
    plt.figure(n)    
    plt.ylabel('y-coordinate [$\lambda_0$]')
    plt.xlabel('x-coordinate [$\lambda_0$]')
    plt.axis('equal')
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,y1 - 2 ,y2 + 2))
    plt.grid()
    plt.show()
    
def plot_data(data, n=2):
    ang = np.arange(0, len(data), 1)
    
    plt.figure(n)
    
    plt.xlabel(r'$\phi$ [degrees]')
    
    #mrpo_plot, = plt.plot(ang, data, label='MRPO', linestyle='-', marker='D', ms=4, markevery=3)
    mrpo_plot, = plt.plot(ang, data, label='MRPO')
    
    plt.grid(True)
    
    plt.ylabel(r'$\sigma_{2D}$ [dB]')
#    plt.legend(handles=[mrpo_plot], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#       ncol=3, mode="expand", borderaxespad=0.)
#    plt.savefig(savePath + "updated_combined_rcs.eps", format='eps', dpi=1200, bbox_inches='tight')
#    print("Saved figure as " + savePath + "updated_combined_rcs.eps")
    print('Image plotted...')