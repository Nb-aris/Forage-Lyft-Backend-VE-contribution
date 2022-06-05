from car import car #TODO!  

from Engine.Capulet_engine import capulet
from Engine.Sternman_engine import sternman
from Engine.Willoughby_engine import willoughby
from Battery.Nubbin import nubbin
from Battery.Spindler import spindler
from Tires.carrigan_tires import CarriganTires
from Tires.octoprime_tires import OctoprimeTires



                

class Model(car):
    """
    Each model have Engine and Battery by default


    parameters = {
        
        'currentDate': None,
        'lastServiceDate': None,
        'currentMiles': None,
        'lastServiceMiles': None
        
        }  
    
    """
    
        
    
    @staticmethod
    def calliope(parameters: dict):
        """
        parameters = {
        
        'currentDate': Value,
        'lastServiceDate': Value,
        'currentMiles': Value,
        'lastServiceMiles': Value
        
        }
        
        """
        carModel = car('calliope')
        
        carModel.initParameters(parameters)
        carModel.setService('engine', capulet(carModel.getParameters()))
        
        carModel.setService('battery', spindler(carModel.getParameters()))
        
        return carModel
        
    
    @staticmethod
    def glissade(parameters: dict):
        """
        parameters = {
        
        'currentDate': Value,
        'lastServiceDate': Value,
        'currentMiles': Value,
        'lastServiceMiles': Value
        
        }
        
        """
        
        carModel = car('calliope')
        
        carModel.initParameters(parameters)
        carModel.setService('engine', willoughby(carModel.getParameters()))
        
        carModel.setService('battery', spindler(carModel.getParameters()))
        
        return carModel
    
    @staticmethod
    def palindrome(parameters: dict):
        """
        parameters = {
        
        'currentDate': Value,
        'lastServiceDate': Value,
        'currentMiles': Value,
        'lastServiceMiles': Value
        
        }
        
        """
        
        carModel = car('calliope')
        
        carModel.initParameters(parameters)
        carModel.setService('engine', sternman(carModel.getParameters()))
        
        carModel.setService('battery', spindler(carModel.getParameters()))
        
        return carModel
    
    @staticmethod
    def rorschach(parameters: dict):
        """
        parameters = {
        
        'currentDate': Value,
        'lastServiceDate': Value,
        'currentMiles': Value,
        'lastServiceMiles': Value
        
        }
        
        """
        carModel = car('calliope')
        
        carModel.initParameters(parameters)
        carModel.setService('engine', willoughby(carModel.getParameters()))
        
        carModel.setService('battery', nubbin(carModel.getParameters()))
        
        return carModel
    
    @staticmethod
    def thovex(parameters: dict):
        """
        parameters = {
        
        'currentDate': Value,
        'lastServiceDate': Value,
        'currentMiles': Value,
        'lastServiceMiles': Value
        
        }
        
        """
        carModel = car('calliope')
        
        carModel.initParameters(parameters)
        carModel.setService('engine', capulet(carModel.getParameters()))
        
        carModel.setService('battery', nubbin(carModel.getParameters()))
        
        return carModel
    
    
    



