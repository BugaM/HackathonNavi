import numpy as np
import pandas as pd

portfolio = pd.read_csv('portfolio.csv')
data = pd.read_csv('selected_prototype_data.csv')
company_ids = portfolio.company_id
risk = []
esg = []
industry = []
for _, row in portfolio.iterrows():
    company = data[data.company_id == row.company_id]
    risk.append(company.risk.values[0])
    esg.append(company.score_value.values[0])
    industry.append(company.industry.values[0])
portfolio['risk'] = risk
portfolio['esg'] = esg
portfolio['industry'] = industry
mean_risk = np.mean(risk)
mean_esg = np.mean(esg)
# risk_influence = (risk*portfolio.qtd - mean_risk)/

