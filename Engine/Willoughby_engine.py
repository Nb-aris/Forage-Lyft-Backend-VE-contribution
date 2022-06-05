#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:18:15 2022

@author: falcon-x
"""

from Engine.engine import Engine

class willoughby(Engine):
    def __init__(self, currentMiles, lastServicedMiles):
        self.currentMiles = currentMiles
        self.lastServicedMiles = lastServicedMiles
        
    def needService(self):
        return self.currentMiles - self.lastServicedMiles > 60000
    
    def getName(self):
        return 'willoughby engine'
    