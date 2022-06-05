from abc import ABC, abstractmethod
from serviceable import Serviceable

class car(Serviceable, ABC):
    def __init__(self, model: str):
        self.model = model
        self.services = {}
        self.parameters : dict

    # @abstractmethod
    def modelName(self):
        return self.model
    
    def serviceAvailable(self, serviceName):
        return self.services[serviceName].getName()

    # @abstractmethod
    def setService(self, serviceName: str, service: object) -> None:
        self.services[serviceName] = service

    # @abstractmethod
    def needService(self):
        for service in self.services.values():
            if service.needService():
                return True
        return False

    # @abstractmethod
    def setParameters(self, parameterName: str, parameterType = None) -> None:
        self.parameters[parameterName] = parameterType
        
    def initParameters(self, parameters):
        self.parameters = parameters
    

