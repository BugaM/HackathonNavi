import numpy as np
import pandas as pd

data = pd.read_csv('data/selected_prototype_data.csv')
industries = []
mean_esg = []
mean_risk = []
for industry in data["industry"].drop_duplicates(keep='first'):
    industries.append(industry)
    mean_esg.append(np.mean(data[data.industry == industry]["score_value"]))
    mean_risk.append(np.mean(data[data.industry == industry]["risk"]))
industries_dataset = pd.DataFrame({"industry": industries, "mean_esg": mean_esg, "mean_risk": mean_esg})
industries_dataset.to_csv('data/prototype_industry_data.csv', index=False)
