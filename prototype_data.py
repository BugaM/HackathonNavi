import pandas as pd
import numpy as np
from yahoo_fin import stock_info
import cufflinks as cf
cf.set_config_file(offline=True)

df_esg = pd.read_csv("data/esg_scores_history_br.csv")
df_risk = pd.read_csv("data/physical_risk_forecast_br.csv")
df_company = pd.read_csv("data/companies_br.csv")

# define which data will be analyzed


# define which ESG score to use
# score_type = 'Environmental Dimension'
score_type = 'S&P Global ESG Score' # regular ESG score

dataset = df_esg[df_esg.aspect == score_type]
dataset = dataset[dataset.assessment_year == 2020]
dataset = dataset[['score_value', 'company_id', 'industry']]
df_risk = df_risk[df_risk.fiscal_year == 2019]
df_risk = df_risk[df_risk.forecast_year == 2050]
df_risk = df_risk[df_risk.scenario_level == 'High']
risk = []
ticker = []
price = []
for _, row in dataset.iterrows():
    value = df_risk[df_risk.company_id == row.company_id]
    if not value.empty:
        risk.append(value.data_item_value.values[0])
    else:
        risk.append(np.NAN)
dataset['risk'] = risk
for _, row in dataset.iterrows():
    value = df_company[df_company.company_id == row.company_id]
    if not value.empty:
        ticker.append(value.ticker.values[0])
    else:
        ticker.append(np.NAN)
dataset['ticker'] = ticker
for _, row in dataset.iterrows():
    try:
        price.append(stock_info.get_live_price((row.ticker+".SA")))
    except:
        price.append(np.NAN)
dataset['price'] = price
dataset = dataset.dropna()
dataset = dataset.drop_duplicates(keep='first')
dataset.to_csv('data/selected_prototype_data.csv', index=False)
