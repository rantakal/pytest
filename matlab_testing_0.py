# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:18:59 2021

@author: kalle
"""

import matlab.engine as engine

print("start")

eng = engine.start_matlab()
eng.cd('C:/Users/kalle/OneDrive/Tiedostot/MATLAB/')

for i in range(1,10):
    a = 1.0
    a = eng.round_area(i)
    print(a)
    
print ("end")