# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:18:21 2017

@author: mrichardson
"""

import math

# Debug level
DEBUG          = 1

# Frequency of simulation
FREQUENCY      = 1e9;

# Incident angle of plane wave
INCIDENT_ANGLE = 0;

# Gaussian quadrature setting
GAUSSIAN_QUADRATURE = 5

# Number of reflections for methods
NUM_MRPO_REFLECTIONS = 7
MAX_IPO_REFLECTIONS = 30
    
# Electromagnetic constants
E_0            = 1
PI             = 3.14159265358979323846;
EPS_0          = 8.854e-12;
MU_0           = PI*4e-7;
C_0            = 1/math.sqrt(EPS_0*MU_0);
LAM_0          = C_0/FREQUENCY;
K_0            = 2*PI/LAM_0;
ETA_0          = math.sqrt(MU_0/EPS_0);
OMEGA          = 2*PI*FREQUENCY;
GAM_0          = 1.781072418

# Maximum size of mesh element
MAX_MESH_SIZE  = LAM_0/10;

# Value for zero (computational errors)
ZERO           = 1e-6

# Start phi value
PHI_START      = 0;
# End phi value
PHI_END        = 180;
# Increment phi value
PHI_INCREMENT  = 1;
# Phi radius
PHI_RADIUS     = 1000*LAM_0;

PLANE_WAVE_SHADOW_DIST = 100*LAM_0