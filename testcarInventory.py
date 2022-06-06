#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:08:17 2022

@author: falcon-x
"""

import unittest

from datetime import datetime

# from car import car

# from Engine.Capulet_engine import capulet
# from Engine.Sternman_engine import sternman
# from Engine.Willoughby_engine import willoughby
# from Battery.Nubbin import nubbin
from Battery.Spindler import spindler
from Tires.carrigan_tires import CarriganTires
from Tires.octoprime_tires import OctoprimeTires

from carFactory import Model

class testcalliope(unittest.TestCase):
    """
    testing bettery: capulet
            engine:spindler
    """
    
    
    i = 1
    
    def testBattery_should_be_serviced(self):
        print ('\n')
        print('..............................testing calliope''\'s'' fleet........................')
        print()
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Battery should be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        car2 = Model.calliope(parameters)
        
        
        
        
        
        self.assertNotEqual(car1, car2, 'checking')
        self.assertEqual(car2.serviceAvailable('engine'), 'capulet engine')
        self.assertEqual(car2.serviceAvailable('battery'), 'spindler battery')
        self.assertEqual(car1.modelName(), car2.modelName())
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
    
        
        
    def testBattery_should_not_be_serviced(self):
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Battery should not be serviced on calliope model...')
        print()
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Engine should be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30001,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Engine should not be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30000,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
        
         
    def testupgradedBattery_should_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if upgrading battery on calliope model possible Test(1)...')
        print()
        
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 4)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.calliope(parameters)
        car1.modifyConst('battery', 3)
        
        
        self.assertTrue(car1.needService())
        
        
        
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
        
    def testupgradedBattery_should_not_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if upgrading battery on calliope model possible(Test 2)...')
        print()
        
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 2)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.calliope(parameters)
        car1.modifyConst('battery', 3)
        
        
        self.assertFalse(car1.needService())
        
        
        
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
        
        
    def testCarrigan_Tires_should_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Carrigan tires should be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        car1.addParameter('tireSensor', [0,0,0,1])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
    def testCarriganTires_should_not_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Carrigan Tires should not be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
    def testOctoprimeTires_should_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Octoprime Tires should be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        car1.addParameter('tireSensor', [1,0,1,1])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
    def testOctoprimeTires_should_not_be_serviced(self):
        
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Octoprime Tires should not be serviced on calliope model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.calliope(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        
        testcalliope.i += 1
        print("- - "*18)
        

class testglissade(unittest.TestCase):
    """
    testing bettery: spindler
            engine:willoughby
    """
    # print('testing model glissade')
    
    i = 11
    def testBattery_should_be_serviced(self):
        print()
        print('.............................testing glissade''\'s'' fleet........................')
        print()
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Battery should be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Battery should not be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Engine should be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60001,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Engine should not be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60000,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testupgradedBattery_should_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if upgrading battery on glissade model possible Test(1)...')
        print()
        
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        car1.modifyConst('battery', 3)
        
        
        self.assertFalse(car1.needService())
        
        
        
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testupgradedBattery_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if upgrading battery on glissade model possible(Test 2)...')
        print()
        
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.glissade(parameters)
        car1.modifyConst('battery', 3)
        
        
        self.assertFalse(car1.needService())
        
        
        
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testCarrigan_Tires_should_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Carrigan tires should be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.glissade(parameters)
        car1.addParameter('tireSensor', [0,0,0,1])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
    def testCarriganTires_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Carrigan Tires should not be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.glissade(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
    def testOctoprimeTires_should_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Octoprime Tires should be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.glissade(parameters)
        car1.addParameter('tireSensor', [1,0,1,1])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
    def testOctoprimeTires_should_not_be_serviced(self):
        
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Octoprime Tires should not be serviced on glissade model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.glissade(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("___"*30, '\n')
        
        testglissade.i += 1
        
class testpalindrome(unittest.TestCase):
    """
    testing bettery: sternman
            engine:spindler
    """
    i = 21
    
    def testBattery_should_be_serviced(self):
        print()
        print('............................testing palindrome''\'s'' fleet........................')
        print()
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Battery should be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        parameters['engineLight'] = True
        car1 = Model.palindrome(parameters)
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Battery should not be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        
        
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Engine should be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        parameters['engineLight'] = True
        car1 = Model.palindrome(parameters)
        
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Engine should not be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        
        
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("___"*30, '\n')
        
        testpalindrome.i += 1
        
    def testCarrigan_Tires_should_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Carrigan tires should be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        car1.addParameter('tireSensor', [0,0,0,1])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
    def testCarriganTires_should_not_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Carrigan Tires should not be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
    def testOctoprimeTires_should_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Octoprime Tires should be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        car1.addParameter('tireSensor', [1,0,1,1])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
    def testOctoprimeTires_should_not_be_serviced(self):
        
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Octoprime Tires should not be serviced on palindrome model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        parameters['engineLight'] = False
        car1 = Model.palindrome(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("___"*30, '\n')
        
        testpalindrome.i += 1

        
class testrorschach(unittest.TestCase):
    """
    testing bettery: capulet
            engine:spindler
    """
    
    i = 29
    
    def testBattery_should_be_serviced(self):
        print()
        print('.......................testing rorschach''\'s'' fleet........................')
        print()
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Battery should be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 5)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.rorschach(parameters)
        
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Battery should not be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.rorschach(parameters)
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Engine should be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60001,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.rorschach(parameters)
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Engine should not be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60000,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = Model.rorschach(parameters)
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("___"*30, '\n')
        
        testrorschach.i += 1
        
        
    def testCarrigan_Tires_should_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Carrigan tires should be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.rorschach(parameters)
        car1.addParameter('tireSensor', [0,0,0,1])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
    def testCarriganTires_should_not_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Carrigan Tires should not be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.rorschach(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
    def testOctoprimeTires_should_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Octoprime Tires should be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.rorschach(parameters)
        car1.addParameter('tireSensor', [1,0,1,1])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
    def testOctoprimeTires_should_not_be_serviced(self):
        
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Octoprime Tires should not be serviced on rorschach model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.rorschach(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("___"*30, '\n')
        
        testrorschach.i += 1

        
class testthovex(unittest.TestCase):
    """
    testing bettery: capulet
            engine:spindler
    """
    
    i = 37
    
    def testBattery_should_be_serviced(self):
        print()
        print('...............................testing thovex''\'s'' fleet........................')
        print()
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Battery should be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 5)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
        
        car1 = Model.thovex(parameters)
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Battery should not be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
        
        car1 = Model.thovex(parameters)
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Engine should be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30001,
            'lastServiceMiles': 0
            }
        
        car1 = Model.thovex(parameters)
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Engine should not be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30000,
            'lastServiceMiles': 0
            }
        
        car1 = Model.thovex(parameters)
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testModifiedParametes(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing changing battery on thovex from nubbin to spindler...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30000,
            'lastServiceMiles': 0
            }
        
        car1 = Model.thovex(parameters)
        
        self.assertEqual(car1.serviceAvailable('battery'), 'nubbin battery')
        
        car1.setService('battery', spindler(parameters))

        self.assertNotEqual(car1.serviceAvailable('battery'), 'nubbin battery')
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testCarrigan_Tires_should_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Carrigan tires should be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.thovex(parameters)
        car1.addParameter('tireSensor', [0,0,0,1])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testCarriganTires_should_not_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Carrigan Tires should not be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.thovex(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', CarriganTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testOctoprimeTires_should_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Octoprime Tires should be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.thovex(parameters)
        car1.addParameter('tireSensor', [1,0,1,1])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testOctoprimeTires_should_not_be_serviced(self):
        
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Octoprime Tires should not be serviced on thovex model...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = Model.thovex(parameters)
        car1.addParameter('tireSensor', [0,0,0,0])
        car1.setService('tire', OctoprimeTires(car1.getParameters()))
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery'),
            'tire type': car1.serviceAvailable('tire')
            }
        
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Successful!\n')
        # print("___"*30, '\n')
        
        testthovex.i += 1

if __name__ == '__main__':
    
    unittest.main(verbosity=2)