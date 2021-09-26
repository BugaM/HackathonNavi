import pandas as pd
import numpy as np

df_esg = pd.read_csv("data/esg_scores_history_rated.csv")
df_env = pd.read_csv("data/environmental_data_history_rated2012.csv")

industry = 'FOA Food Products'  # defines industry

# define which data will be analyzed
# data_item = 'Impact Ratio: Air Pollutants Direct & Indirect Cost'
data_item = 'Company Revenue'  # used for plot_esg_growth

# define which ESG score to use
# score_type = 'Environmental Dimension'
score_type = 'S&P Global ESG Score'  # regular ESG score

df_esg = df_esg[df_esg.industry == industry]
# use only recent data
if data_item != 'Company Revenue':
    df_esg = df_esg[df_esg.assessment_year == 2020]
df_env = df_env[df_env.data_item_name == data_item]
dataset = df_esg[df_esg.aspect == score_type]
dataset = dataset[['score_value', 'assessment_year', 'company_id']]
item_value = []
for _, row in dataset.iterrows():
    value = df_env[df_env.fiscal_year == row.assessment_year - 1]
    value = value[value.company_id == row.company_id]
    if not value.empty:
        item_value.append(value.data_item_value.values[0])
    else:
        item_value.append(np.NAN)

dataset['item_value'] = item_value

dataset = dataset.sort_values(by=['company_id', 'assessment_year'])

if data_item == 'Company Revenue':
    id = 0
    growth_list = []
    for _, row in dataset.iterrows():
        if id != row.company_id:
            id = row.company_id
            base_item_value = row.item_value
            growth = 0
            if row.assessment_year == 2013:
                valid = True
            else:
                valid = False
        else:
            growth = row.item_value / base_item_value - 1
        if valid:
            growth_list.append(growth)
        else:
            growth_list.append(np.NAN)
    dataset['growth'] = growth_list

dataset = dataset.dropna()
dataset = dataset.drop_duplicates(keep='first')
dataset.to_csv('selected_data.csv', index=False)
