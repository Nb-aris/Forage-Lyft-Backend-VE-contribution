#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:43:07 2022

@author: falcon-x
"""

from abc import ABC, abstractmethod


class Engine():
    
    def __init__(self):
        
        pass
    
    @abstractmethod
    def needService(self):
        pass
        

    
