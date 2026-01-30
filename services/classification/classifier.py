from abc import ABC, abstractmethod

class TicketClassifier(ABC):

    @abstractmethod
    def classify(self, description: str) -> str:
        pass