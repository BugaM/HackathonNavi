import numpy as np
import pandas as pd

portfolio = pd.read_csv('data/portfolio.csv')
data = pd.read_csv('data/selected_prototype_data.csv')
risk = []
esg = []
industry = []
stocks_worth = []
portfolio_worth = 0
for _, row in portfolio.iterrows():
    company = data[data.ticker == row.ticker]
    if not company.empty:
        risk.append(company.risk.values[0])
        esg.append(company.score_value.values[0])
        industry.append(company.industry.values[0])
        stocks_worth.append(company.price.values[0]*row.quantity)
        portfolio_worth += company.price.values[0]*row.quantity
    else:
        print("Não há informação suficiente sobre o ativo {}.".format(row.ticker))
        risk.append(np.NAN)
        esg.append(np.NAN)
        industry.append(np.NAN)
        stocks_worth.append(np.NAN)
portfolio['risk'] = risk
portfolio['esg'] = esg
portfolio['industry'] = industry
portfolio['stocks_worth'] = stocks_worth
portfolio = portfolio.dropna()
mean_esg = 0
mean_risk = 0
for _, row in portfolio.iterrows():
    mean_esg += row.stocks_worth*row.esg
    mean_risk += row.stocks_worth*row.risk
mean_esg = mean_esg/portfolio_worth
mean_risk = mean_risk/portfolio_worth
esg_impact = []
risk_impact = []
for _, row in portfolio.iterrows():
    esg_impact.append(row.stocks_worth*(row.esg - mean_esg)/portfolio_worth)
    risk_impact.append(row.stocks_worth*(row.risk - mean_risk)/portfolio_worth)
portfolio['esg_impact'] = esg_impact
portfolio['risk_impact'] = risk_impact
print("O valor total da carteira é {:.2f} BRL, sua média ESG é {:.2f} e seu risco médio é {:.2f}.".format(portfolio_worth, mean_esg, mean_risk))
portfolio.to_csv('data/portfolio_analytics.csv', index=False)
