import pandas as pd
# used to reduce datasets

csv = pd.read_csv('data/environmental_data_history_rated.csv')
csv = csv.drop(csv[csv.fiscal_year < 2012].index)


csv.to_csv('environmental_data_history_rated2012.zip', index=False)
