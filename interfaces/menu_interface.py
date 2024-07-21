from abc import ABC, abstractmethod

class MenuInterface(ABC):
    @abstractmethod
    def run(self):
        pass
