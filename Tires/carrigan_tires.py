#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:52:52 2022

@author: falcon-x
"""
from Tires.tyre import Tyre


class CarriganTires(Tyre):
    def __init__(self, parameter):
        # assert(len(four_tires) == 4)
        self.four_tires = parameter['tireSensor']

    def needService(self):
        return sum(x >= 0.9 for x in self.four_tires) > 0
    
    def getName(self):
        return 'carrigan tires'
    