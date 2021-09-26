import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

csv = 'selected_data.csv'
title = 'Impact Ratio: Air Pollutants Direct & Indirect Cost'
score_type = 'Environmental Dimension'
industry = 'FOA'

df = pd.read_csv(csv)
X = df.score_value.values.reshape(-1, 1)  # values converts it into a numpy array
Y = df.item_value.values.reshape(-1, 1)

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

r2 = r2_score(Y, Y_pred)
print(r2) # r2 for statistical relevance


plt.plot(X, Y_pred, color='red')
plt.scatter(X, Y)
plt.xlabel(score_type)
plt.ylabel('Impact')
plt.grid()
plt.title('Impact Ratio: Air Pollutants Direct & Indirect Cost - ' +  industry)
plt.savefig(title + '.png')
plt.show()
