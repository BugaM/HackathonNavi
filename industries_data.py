import numpy as np
import pandas as pd

data = pd.read_csv('data/selected_prototype_data.csv')
industries = []
mean_esg = []
max_esg = []
min_esg = []
mean_risk = []
max_risk = []
min_risk = []
for industry in data["industry"].drop_duplicates(keep='first'):
    industries.append(industry)
    mean_esg.append(np.mean(data[data.industry == industry]["score_value"]))
    max_esg.append(np.max(data[data.industry == industry]["score_value"]))
    min_esg.append(np.min(data[data.industry == industry]["score_value"]))
    mean_risk.append(np.mean(data[data.industry == industry]["risk"]))
    max_risk.append(np.max(data[data.industry == industry]["risk"]))
    min_risk.append(np.min(data[data.industry == industry]["risk"]))
industries_dataset = pd.DataFrame({"industry": industries, "mean_esg": mean_esg, "max_esg": max_esg, "min_esg": min_esg,
                                  "mean_risk": mean_risk, "max_risk": max_risk, "min_risk": min_risk})
industries_dataset.to_csv('data/prototype_industry_data.csv', index=False)
