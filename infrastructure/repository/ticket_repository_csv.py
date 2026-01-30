import pandas as pd

class TicketRepositoryCSV:

    def load(self) -> pd.DataFrame:
        return pd.read_csv("data/tickets.csv")
