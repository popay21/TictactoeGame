from abc import ABC, abstractmethod

class EndInterface(ABC):
    @abstractmethod
    def run(self, winner):
        pass
