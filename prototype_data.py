import pandas as pd
import numpy as np

df_esg = pd.read_csv("esg_scores_history_rated.csv")
df_risk = pd.read_csv("physical_risk_forecast_rated.csv")

industry = 'FOA Food Products'  # defines industry

# define which data will be analyzed


# define which ESG score to use
# score_type = 'Environmental Dimension'
score_type = 'S&P Global ESG Score' # regular ESG score

# df_esg = df_esg[df_esg.industry == industry]
dataset = df_esg[df_esg.aspect == score_type]
dataset = dataset[dataset.assessment_year == 2020]
dataset = dataset[['score_value', 'company_id', 'industry']]
df_risk = df_risk[df_risk.fiscal_year == 2019]
df_risk = df_risk[df_risk.forecast_year == 2050]
df_risk = df_risk[df_risk.scenario_level == 'High']
risk = []
for _, row in dataset.iterrows():
    value = df_risk[df_risk.company_id == row.company_id]
    if not value.empty:
        risk.append(value.data_item_value.values[0])
    else:
        risk.append(np.NAN)

dataset['risk'] = risk

dataset = dataset.dropna()
dataset = dataset.drop_duplicates(keep='first')
dataset.to_csv('selected_prototype_data.csv', index=False)
