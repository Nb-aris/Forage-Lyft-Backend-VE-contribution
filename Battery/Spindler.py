#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:35:51 2022

@author: falcon-x
"""

from Battery.battery import Battery

from datetime import datetime

class spindler(Battery):
    def __init__(self, current_service_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date
        
    def needService(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_service_date: #datetime.today().date():
            return True
        return False
    
    def getName(self):
        return 'spindler battery'