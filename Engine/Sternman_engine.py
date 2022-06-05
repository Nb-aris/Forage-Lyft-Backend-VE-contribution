#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:17:52 2022

@author: falcon-x
"""

from Engine.engine import Engine

class sternman(Engine):
    def __init__(self, parameter):
        self.WarningLightsOn = parameter['engineLight']
        
    def needService(self):
        if self.WarningLightsOn:
            return True
        return False
    def getName(self):
        return 'sternman engine'