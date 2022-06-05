#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:08:17 2022

@author: falcon-x
"""

import unittest

from datetime import datetime

from car import car

# from Engine.Capulet_engine import capulet
# from Engine.Sternman_engine import sternman
# from Engine.Willoughby_engine import willoughby
# from Battery.Nubbin import nubbin
# from Battery.Spindler import spindler
# from Tires.carrigan_tires import CarriganTires
# from Tires.octoprime_tires import OctoprimeTires

from carInvetory import capulet, sternman, willoughby, nubbin, spindler

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
        print(f'[{self.i}] testing if Battery should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = car('calliope')
        car2 = car('calliope')
        
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        car2.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car2.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        # self.assertEqual(car1, car2, 'checking')
        self.assertNotEqual(car2.serviceAvailable('engine'), 'capulet engine')
        self.assertNotEqual(car2.serviceAvailable('battery'), 'spindler battery')
        self.assertEqual(car1.modelName(), car2.modelName())
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        return
        
        
    def testBattery_should_not_be_serviced(self):
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Battery should not be serviced...')
        print()
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        car1 = car('calliope')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Engine should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30001,
            'lastServiceMiles': 0
            }
    
        
        car1 = car('calliope')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testcalliope.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testcalliope.i
        print(f'[{self.i}] testing if Engine should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30000,
            'lastServiceMiles': 0
            }
    
        
        car1 = car('calliope')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("___"*30, '\n')
        
        testcalliope.i += 1

class testglissade(unittest.TestCase):
    """
    testing bettery: spindler
            engine:willoughby
    """
    # print('testing model glissade')
    
    i = 1
    
    def testBattery_should_be_serviced(self):
        print()
        print('.............................testing glissade''\'s'' fleet........................')
        print()
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Battery should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('glissade')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Battery should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('glissade')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Engine should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()

        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60001,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('glissade')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testglissade.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testglissade.i
        print(f'[{self.i}] testing if Engine should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60000,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('glissade')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("___"*30, '\n')
        
        testglissade.i += 1
        
class testpalindrome(unittest.TestCase):
    """
    testing bettery: sternman
            engine:spindler
    """
    i = 1
    
    def testBattery_should_be_serviced(self):
        print()
        print('............................testing palindrome''\'s'' fleet........................')
        print()
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Battery should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('palindrome')
        
        parameters['engineLight']  = True
        
        car1.setService('engine', sternman(parameters['engineLight']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Battery should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 1)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('palindrome')
        
        parameters['engineLight']  = False
        
        car1.setService('engine', sternman(parameters['engineLight']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Engine should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('palindrome')
        
        parameters['engineLight']  = True
        
        car1.setService('engine', sternman(parameters['engineLight']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testpalindrome.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testpalindrome.i
        print(f'[{self.i}] testing if Engine should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('palindrome')
        
        parameters['engineLight']  = False
        
        car1.setService('engine', sternman(parameters['engineLight']))
        car1.setService('battery', spindler(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("___"*30, '\n')
        
        testpalindrome.i += 1

        
class testrorschach(unittest.TestCase):
    """
    testing bettery: capulet
            engine:spindler
    """
    
    i = 1
    
    def testBattery_should_be_serviced(self):
        print()
        print('.......................testing rorschach''\'s'' fleet........................')
        print()
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Battery should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 5)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('rorschach')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Battery should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('rorschach')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Engine should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60001,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('rorschach')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testrorschach.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testrorschach.i
        print(f'[{self.i}] testing if Engine should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 60000,
            'lastServiceMiles': 0
            }
    
        
        
        car1 = car('rorschach')
        
        car1.setService('engine', willoughby(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("___"*30, '\n')
        
        testrorschach.i += 1

        
class testthovex(unittest.TestCase):
    """
    testing bettery: capulet
            engine:spindler
    """
    
    i = 1
    
    def testBattery_should_be_serviced(self):
        print()
        print('...............................testing thovex''\'s'' fleet........................')
        print()
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Battery should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 5)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
        
        car1 = car('thovex')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
        
    def testBattery_should_not_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Battery should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = today.replace(year = today.year - 3)
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 0,
            'lastServiceMiles': 0
            }
        
        car1 = car('thovex')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
    def testEngine_should_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Engine should be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30001,
            'lastServiceMiles': 0
            }
        
        car1 = car('thovex')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertTrue(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        print("- - "*18)
        
        testthovex.i += 1
        
        
    def testEngine_should_not_be_serviced(self):
        
        self.i = testthovex.i
        print(f'[{self.i}] testing if Engine should not be serviced...')
        print()
        
        today = datetime.today().date()
        last_serv_date = datetime.today().date()
        
        parameters = {
            
            'currentDate': today,
            'lastServiceDate': last_serv_date,
            'currentMiles': 30000,
            'lastServiceMiles': 0
            }
        
        car1 = car('thovex')
        
        car1.setService('engine', capulet(parameters['currentMiles'], parameters['lastServiceMiles']))
        car1.setService('battery', nubbin(parameters['currentDate'], parameters['lastServiceDate']))
        
        self.assertFalse(car1.needService())
        
        details = {
            'engine type': car1.serviceAvailable('engine'), 
            'battery type': car1.serviceAvailable('battery')
            }
        
        print('\tdetails : ', details, '\n')
        print(f'>>> Test[{self.i}] Succesful!\n')
        # print("- - "*18)
        
        testthovex.i += 1


if __name__ == '__main__':
    
    unittest.main(verbosity=2)