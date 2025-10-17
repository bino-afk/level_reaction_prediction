# level_reaction_prediction
Time series (Conv1D) Neural Network model with stock data engineered to be near key levels, thus training a level reaction predictor

## Dataset

Rows are different instances of stocks with:
* OHLC data
* Computed (or pre-existing) support/resistance levels
* A target column: reaction = 1 for bounce, -1 for break
  * or scalar [-1, 1] for velocity of reaction based off of price change inside prediction window
* Chart time interval either:
  * Column value
  * Preprocess that only accepts the same time value
     * Analyse impact on performance
   

