import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

csv = 'selected_data.csv' # csv data
esg_criteria = 80  # minimal rating to consider a company ESG

df = pd.read_csv(csv)
esg = df[df.score_value >= esg_criteria]
no_esg = df[df.score_value < esg_criteria]

X_esg = esg.assessment_year.values.reshape(-1, 1) - 2013 # values converts it into a numpy array
Y_esg = esg.growth.values.reshape(-1, 1) # -1 means that calculate the dimension of rows, but have 1 column

linear_regressor = LinearRegression(fit_intercept=False)  # create object for the class
linear_regressor.fit(X_esg, Y_esg)  # perform linear regression
Y_pred_esg = linear_regressor.predict(X_esg)  # make predictions

X_no_esg = no_esg.assessment_year.values.reshape(-1, 1) - 2013  # values converts it into a numpy array
Y_no_esg = no_esg.growth.values.reshape(-1, 1)


linear_regressor.fit(X_no_esg, Y_no_esg)  # perform linear regression
Y_pred_no_esg = linear_regressor.predict(X_no_esg)  # make predictions

r2_esg = r2_score(Y_esg, Y_pred_esg)
r2_no_esg = r2_score(Y_no_esg, Y_pred_no_esg)

print(r2_esg, r2_no_esg)

plt.plot(X_esg, Y_pred_esg, color='red', label='ESG')
# plt.scatter(X_esg,Y_esg, color='red')
plt.plot(X_no_esg, Y_pred_no_esg, color='blue', label='non-ESG')
# plt.scatter(X_no_esg,Y_no_esg, color='blue')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Growth (reference year: 2013)')
plt.title('ESG vs non ESG companies revenue growth')
plt.grid()
plt.savefig('MNX_Growth.png')
plt.show()
