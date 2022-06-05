#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:43:40 2022

@author: falcon-x
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Tyre(ABC):
    
    @abstractmethod
    def needService(self):
        pass
    

