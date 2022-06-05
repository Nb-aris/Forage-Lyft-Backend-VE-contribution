#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:35:31 2022

@author: falcon-x
"""

from abc import ABC, abstractmethod

class Battery(ABC):
        
    @abstractmethod
    def needService(self):
        pass
    