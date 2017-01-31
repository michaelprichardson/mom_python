# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:44:57 2017

@author: michael
"""

import numpy as np

pi              = np.pi
eps0            = 8.854e-12
mu0             = 4*pi*1e-7
c0              = 2.99792458e8
freq            = 300e6
freq_range      = [150e6, 50e6, 450e6]
lam0            = c0/freq
k0              = 2*pi/lam0
eta0            = np.sqrt(mu0/eps0)
gam             = 1.781072418
phi_inc         = 0

num_fieldpoints = 360
phi_fieldpoints = np.arange(0, pi, pi/num_fieldpoints)
rad_fieldpoints = 100*lam0
line_length     = 10*lam0

meshsize_solve  = lam0/10

plot_angs       = np.arange(0, 180, 0.5)