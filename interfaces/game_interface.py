from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def run(self):
        pass
