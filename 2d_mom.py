# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:23:40 2017

@author: mrichardson
"""

import point
import segment
import create_mesh as mesh
import plot
import calculate_mom_data as mom

# Build geometry and mesh
geometry = [mesh.create_line(), mesh.create_reflector(), mesh.create_circle(), mesh.create_line_with_angled_edge()]

# Select a geometry to use
msh = geometry[0]

# Calculate the scatter field using Method of Moments
data = mom.calculate_mom(msh)

# Plot data
plot.plot_mesh(msh)
plot.plot_data(data)