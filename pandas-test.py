import pandas as pd

config_df = pd.read_csv('market-cap50.csv', delimiter=",", names=["sector","symbol", "value"])
configs = dict(zip(config_df.sector, config_df.symbol, config_df.value))
print (configs)

