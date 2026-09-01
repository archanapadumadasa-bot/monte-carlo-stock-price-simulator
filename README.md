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

