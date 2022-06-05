#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:52:52 2022

@author: falcon-x
"""
from Tires.tyre import Tyre


class CarriganTires(Tyre):
    def __init__(self, four_tires):
        assert(len(four_tires) == 4)
        self.four_tires = four_tires

    def needService(self):
        return sum(x >= 0.9 for x in self.four_tires) > 0
    