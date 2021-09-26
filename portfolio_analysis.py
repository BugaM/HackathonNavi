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
suggestions_df = pd.DataFrame(columns=['ticker', 'risk', 'score_value', 'industry'])
for index, row in portfolio.iterrows():
    current_risk = risk[index]
    current_esg = esg[index]
    options = data[data.industry == row.industry]
    options = options[options.risk < current_risk]
    options = options[['score_value', 'ticker', 'risk', 'industry']]
    options.sort_values(by=['score_value'])
    if not options.empty:
        suggestions_df = suggestions_df.append(options.head(1), ignore_index=True)


print("O valor total da carteira é {:.2f} BRL, sua média ESG é {:.2f} e seu risco médio é {:.2f}.".format(portfolio_worth, mean_esg, mean_risk))
for _, row in suggestions_df.iterrows():
    print('You should consider ' + row.ticker + ' as an option in the ' + row.industry + ' industry')
suggestions_df.to_csv('data/portfolio_suggestions.csv')
print('Suggested options have been exported')
portfolio.to_csv('data/portfolio_analytics.csv', index=False)
