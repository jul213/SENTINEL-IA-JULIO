import pandas as pd

class SecurityEngine:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

    def get_critical_threats(self):
        # Filtramos ataques críticos usando Big Data (Pandas)
        critical = self.df[self.df['action'] == 'BLOCK']
        return critical.sort_values(by='bytes_sent', ascending=False).head(10)

    def stats(self):
        # Estadísticas rápidas para el Dashboard
        return self.df['threat_type'].value_counts()