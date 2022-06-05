#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:53:15 2022

@author: falcon-x
"""

from Tires.tyre import Tyre


class OctoprimeTires(Tyre):
    def __init__(self, four_tires):
        # assert(len(four_tires) == 4)
        self.four_tires = four_tires

    def needsService(self):
        return sum(self.four_tires) >= 3