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

