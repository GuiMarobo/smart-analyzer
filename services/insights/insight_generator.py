from abc import ABC, abstractmethod
import pandas as pd

class InsightGenerator(ABC):

    @abstractmethod
    def generate(self, df: pd.DataFrame) -> list[str]:
        pass
