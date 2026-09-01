"""
Monte Carlo Stock Price Predictor
-----------------------------------
Reads historical daily stock prices from a CSV, calculates how often
the price goes up, down, or stays the same, then uses that to run
thousands of randomly simulated future price paths (Monte Carlo
simulation) to estimate a range of possible future prices.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read Data

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df



# % Change Calculation and Categorization

def calculate_pct_change(df):
    df['prev_price'] = df['price'].shift(1)
    df['pct_change'] = (df['price'] - df['prev_price']) / df['prev_price'] * 100
    df = df.dropna(subset=['pct_change'])  
    return df


def classify_direction(df):
    def classify(x):
        if x > 0:
            return 'increase'
        elif x < 0:
            return 'decrease'
        else:
            return 'unchanged'
    df['direction'] = df['pct_change'].apply(classify)
    return df


def summarize(df):
    total = len(df)
    n_increase = (df['direction'] == 'increase').sum()
    n_decrease = (df['direction'] == 'decrease').sum()
    n_unchanged = (df['direction'] == 'unchanged').sum()

    pct_increase = (n_increase / total) * 100
    pct_decrease = (n_decrease / total) * 100
    pct_unchanged = (n_unchanged / total) * 100

    print(f"Total days: {total}")
    print(f"% increase days: {pct_increase:.2f}%")
    print(f"% decrease days: {pct_decrease:.2f}%")
    print(f"% unchanged days: {pct_unchanged:.2f}%")

    return pct_increase, pct_decrease, pct_unchanged


# Normal Distribution

def calculate_distributions(df):
    increase_days = df[df['direction'] == 'increase']['pct_change']
    decrease_days = df[df['direction'] == 'decrease']['pct_change']

    increase_mean = increase_days.mean()
    increase_std = increase_days.std()
    decrease_mean = decrease_days.mean()
    decrease_std = decrease_days.std()

    print(f"Increase days -> mean: {increase_mean:.4f}%, std: {increase_std:.4f}%")
    print(f"Decrease days -> mean: {decrease_mean:.4f}%, std: {decrease_std:.4f}%")

    return increase_mean, increase_std, decrease_mean, decrease_std


# Monte Carlo Simulation

def run_simulation(start_price, pct_increase, pct_decrease, pct_unchanged,
                    inc_mean, inc_std, dec_mean, dec_std,
                    horizon_days, n_simulations):
    
    p_up = pct_increase / 100
    p_down = pct_decrease / 100
    p_unchanged = pct_unchanged / 100

    final_prices = []

    for sim in range(n_simulations):
        price = start_price
        for day in range(horizon_days):
            r = np.random.random()
            if r < p_up:
                pct_move = np.random.normal(inc_mean, inc_std)
            elif r < p_up + p_down:
                pct_move = np.random.normal(dec_mean, dec_std)
            else:
                pct_move = 0  
            price = price * (1 + pct_move / 100)
        final_prices.append(price)

    return final_prices


# Simulation Results

def percentile_bands(final_prices):
    final_prices = np.array(final_prices)
    p5 = np.percentile(final_prices, 5)
    p25 = np.percentile(final_prices, 25)
    p50 = np.percentile(final_prices, 50)
    p75 = np.percentile(final_prices, 75)
    p95 = np.percentile(final_prices, 95)

    print(f"5th percentile: {p5:.2f}")
    print(f"25th percentile: {p25:.2f}")
    print(f"50th percentile (median): {p50:.2f}")
    print(f"75th percentile: {p75:.2f}")
    print(f"95th percentile: {p95:.2f}")


def outcome_stats(final_prices, start_price):
    final_prices = np.array(final_prices)
    n = len(final_prices)

    n_losses = (final_prices < start_price).sum()
    n_profits = (final_prices > start_price).sum()

    pct_losses = (n_losses / n) * 100
    pct_profits = (n_profits / n) * 100

    print(f"% of simulations with a loss: {pct_losses:.2f}%")
    print(f"% of simulations with a profit: {pct_profits:.2f}%")

    return pct_losses, pct_profits


def return_threshold_breakdown(final_prices, start_price, thresholds):
    final_prices = np.array(final_prices)
    n = len(final_prices)

    results = {}
    for pct in thresholds:
        threshold_price = start_price * (1 + pct / 100)
        n_above = (final_prices > threshold_price).sum()
        pct_above = (n_above / n) * 100
        print(f"% of simulations with return > {pct}%: {pct_above:.2f}%")
        results[pct] = pct_above

    return results


# Histogram of results

def plot_histogram(final_prices, start_price):
    plt.figure(figsize=(10, 6))
    plt.hist(final_prices, bins=50, color='steelblue', edgecolor='black')
    plt.axvline(start_price, color='red', linestyle='--', linewidth=2, label=f'Starting price: {start_price:.2f}')
    plt.title('Monte Carlo Simulation: Distribution of Simulated Future Prices')
    plt.xlabel('Simulated Price')
    plt.ylabel('Number of Simulations')
    plt.legend()
    plt.tight_layout()
    plt.savefig('simulation_histogram.png')
    print("\nHistogram saved as 'simulation_histogram.png'")
    plt.show()


# MAIN PROGRAM

CSV_PATH = "sample_stock.csv"
RETURN_THRESHOLDS = [20, 30, 40, 50]   

horizon_days = int(input("How many days into the future should the simulation project? "))
n_simulations = int(input("How many simulations should be run? "))

df = load_data(CSV_PATH)
df = calculate_pct_change(df)
df = classify_direction(df)
pct_increase, pct_decrease, pct_unchanged = summarize(df)

inc_mean, inc_std, dec_mean, dec_std = calculate_distributions(df)

start_price = df['price'].iloc[-1]

final_prices = run_simulation(
    start_price=start_price,
    pct_increase=pct_increase,
    pct_decrease=pct_decrease,
    pct_unchanged=pct_unchanged,
    inc_mean=inc_mean, inc_std=inc_std,
    dec_mean=dec_mean, dec_std=dec_std,
    horizon_days=horizon_days,
    n_simulations=n_simulations
)

print(f"\nStarting price: {start_price:.2f}")
print(f"Mean final price: {np.mean(final_prices):.2f}")
print(f"Median final price: {np.median(final_prices):.2f}")

percentile_bands(final_prices)
outcome_stats(final_prices, start_price)
return_threshold_breakdown(final_prices, start_price, RETURN_THRESHOLDS)

plot_histogram(final_prices, start_price)
