from abc import ABC, abstractmethod
from serviceable import Serviceable

class car(Serviceable, ABC):
    def __init__(self, model: str):
        self.model = model
        self.services = {}
        self.parameters : dict = None

    # @abstractmethod
    def modelName(self):
        return self.model
    
    def serviceAvailable(self, serviceName):
        return self.services[serviceName].getName()

    # @abstractmethod
    def setService(self, serviceName: str, service: object) -> None:
        self.services[serviceName] = service
        
    def modifyConst(self, serviceName: str, modification) -> None:
        self.services[serviceName].modifyConst(modification)


    # @abstractmethod
    def addParameter(self, parameterName: str, parameterValue) -> None:
        self.parameters[parameterName] = parameterValue
        
    # @abstractmethod
    def getParameters(self):
        return self.parameters
        
    def initParameters(self, parameters):
        self.parameters = parameters
    
    # @abstractmethod
    def needService(self):
        for service in self.services.values():
            if service.needService():
                return True
        return False

