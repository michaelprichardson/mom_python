# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 16:51:52 2017

@author: mrichardson
"""

import gaussian_quadrature as gq

gaus = gq.getGaussianQuadrature(2)

x1 = 3.0
y1 = 3.0

x2 = 5.0
y2 = 5.0

real_mid_x = (x1 + x2)/2 
real_mid_y = (y1 + y2)/2 

print("mid x: {:f} mid y {:f}".format(real_mid_x, real_mid_y))

gaus_mid_x = (x1 + x2*gaus[0][1])/2 
gaus_mid_y = (y1 + y2*gaus[0][1])/2 

print("mid x: {:f} mid y {:f}".format(gaus_mid_x, gaus_mid_y))

gaus_mid_x = gaus_mid_x + (x1*gaus[0][1] + x2*gaus[1][1])/2 
gaus_mid_y = gaus_mid_y + (y1*gaus[0][1] + y2*gaus[1][1])/2 

print("mid x: {:f} mid y {:f}".format(gaus_mid_x, gaus_mid_y))