# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:48:48 2020

@author: Alex
"""

from conway_models.cw3d import conway_grid_3d
from conway_models.cw4d import conway_grid_4d

file = 'input.txt'
conway3d=conway_grid_3d(file)
print('')
conway4d=conway_grid_4d(file)




