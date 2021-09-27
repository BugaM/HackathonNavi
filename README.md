# Navi Tech Journey Team 12 - Arbor

Code by:

- Eric Guerra Ribeiro
- Marcelo Buga Martins da Silva

## External Dependencies

- numpy
- pandas
- yahoo fin
- cufflinks

It is also necessary to add the S&P database to the data folder to generate the database used by the portfolio analytics. Only the csv files about Brazillian companies are needed.

## How to Run

For convenience, the generated datasets are already in the github repository. So if getting the current stock prices is not needed, you may skip the next step.
First step, run the ```create_datasets.py```. It may take a while as the yahoo finance API is quite slow. It will generate a dataset with the companies in IBOVESPA which all relevant ESG and risk data is known. It will also generate a dataset that compiles risk and ESG data from all companies by industry.
After that add each assets of portfolio in each line of the ```data/portfolio.txt``` file. The asset should be represented by its IBOVESPA symbol and the quantity held, separated by a blanck space. For instance, if you own 100 stocks of the mining company Vale, that asset should be represented by "VALE3 100".
Then, generate a csv file that represents your portfolio by running the file ```portfolio_creation.py```.
Finally, run the ```portfolio_analysis.py``` file. It will calculate and show, how much the portfolio is worth, the weighted by value average ESG score and a pessimistic climatic risk forecast up to 2030.
It will also check if there are companies which ESG score is higher and climatic risk lower than a company in the portfolio from the same industry. If so, its stock is shown and added to a database. Other than that, it generates a more detailed, albeit still simple analysis of each stock ESG and risk. In that database, it is shown the ESG scores and climatic risk for each stock and how it compares to the average in its industry. The impact of the asset in your ESG compliance and in your portfolio risk, i.e., how it deviates from the average ESG score and risk.

## Future Improvements

The main flaw would be the lack of an interative frontend interface in which you could change your portfolio easily and see the results of the analysis. However, the way the code is done using csv files as interfaces between different codes, the frontend app would only need to generate a csv file with the portfolio and read the analysis made by the code.
