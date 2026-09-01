# Monte Carlo Stock Price Simulator
A python tool that models the future price of a stock as a range of outcomes using Monte Carlo simulation driven by historical daily stock price data.

Built as a personal project ahead of starting an economics degree at the University College London (UCL).

---
## Table of Contents
[What It Does](#what-it-does)

[Methodology](#methodology)

[Why Two Separate Distributions?](#why-two-separate-distributions)

[Assumptions and Limitations](#assumptions-and-limitations)

[How to Run It](#how-to-run-it)

[Possible Extensions](#possible-extensions)

---
## What it does
This model uses historical daily stock price data extracted from a CSV file and estimates the future price range of given stock after a selected number of trading days. Results are then expressed as a probability distribution.

The model reports;

-The probability of an up day or a down day 

-Estimated Stock Prices for specific percentiles

-Probability of hitting specific return thresholds

-Histogram displaying full spread of simulated outcomes

## Methodology
-Historical Daily Stock Closing Prices are extracted from a CSV File containing two columns, date and stock price.

-The daily percentage change in stock price is calculated for each consecutive day.

-Each percentage change is categorized as increase (up-day), decrease (down-day) and unchanged.

-Two normal distributions are created, one for all the percentage change values for up-days and one for all the percentage change values for down days.

-Simulation is run. Thousands of independent future pathways is taken, where based on historical probability each future trading day randomly is predicted an increased, decreased or unchanged stock price. Magnitude of change in stock price is randomly determined based on the relevant normal distribution. 

-Results across every simulated pathway is aggregated a distribution of final prices is produced in form of a histogram and a overall report is created.

## Why two separate normal distributions?
Most introductory Monte Carlo models draws from a single normal distribution with the assumption that magnitude of up-days and down-days are perfectly symmetric. 

This project instead produces a separate normal distribution for magnitude of up-days and magnitude of down-days. This allows more accurate estimations to be made since in a real world application, a stock's typical rally size often differs from a stock's typical drawdown size. 

## Assumptions and Limitations

-Percentage Changes in stock price is assumed to follow a normal distribution. However, when applied in the real world, distribution of percentage changes in stock prices is often fatter tailed. Hence, this model predicts a large change in stock price far less frequently than what is actually seen in a stock market.

-Only input taken into account is historical daily stock closing prices. Trading Volume, Macroeconomic Factors, Company Fundamentals, Current Affairs are not taken into account. However, these other factors also play a crucial part in stock prices, hence, for a more accurate model, some of these factors may need to be incorporated.

-Each simulated day is independent, hence does not account for volatility clustering which is often seen in real markets where big changes in stock prices are often followed by further big changes.

-This model can only make predictions based on statistical methods.

## How to Run it 
-Requirements : pip3 install pandas numpy matplotlib

-Run : python3 montecarlostocksimulator.py (has been attached in the repository)

-Answer the prompts on how many trading days into the future the model should simulate and how many simulations the model should carry out.

-Input data format: A CSV file containing two columns (date, price) for the given stock should be placed in the same folder as montecarlosimulator.py. For example, sample_stock.csv which is attached in the repository (this is a synthetic sample data set). When using different csv file, change text given beside CSV_PATH in the python program. 

## Sample Output
Report containing 

- % of up-days, % of down-days, % of unchanged days
  
- Mean and Standard Deviation for each normal distrbituon for up-days and down-days
  
- Starting Price, Mean Final Price, Median Final Price
  
- Stock Price that falls under specific percentiles
  
- % of simulations that made losses vs % of simulations that made profits
  
- % of simulations that hit specific return thresholds
  
- Histogram showing distribution of simulated stock prices.
  
The overall report can be seen in "Monte Carlo Simulation Results.png" attached in the repository, while the histogram can be seen in "simulation_hisogram.png" attached in the repository.

