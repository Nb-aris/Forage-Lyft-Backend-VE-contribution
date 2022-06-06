#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:53:15 2022

@author: falcon-x
"""

from Tires.tyre import Tyre


class OctoprimeTires(Tyre):
    def __init__(self, parameter):
        # assert(len(four_tires) == 4)
        self.four_tires = parameter['tireSensor']

    def needService(self):
        return sum(self.four_tires) >= 3
    
    def getName(self):
        return 'octoprime tires'