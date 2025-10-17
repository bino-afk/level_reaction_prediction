# level_reaction_prediction
Time series (Conv1D) Neural Network model with stock data engineered to be near key levels, thus training a level reaction predictor

Step 1: Define the dataset

Rows of columns are different instances of stocks with:
* OHLC data
* Computed (or pre-existing) support/resistance levels
* A target column: reaction = 1 for bounce, -1 for break
** (or scalar for velocity of reaction based off of price change inside prediction window)

