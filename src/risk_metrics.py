import numpy as np

def calculate_daily_returns(prices):

    daily_returns = prices.pct_change().dropna()

    return daily_returns

def calculate_rolling_volatility(daily_returns, window=21):

    rolling_volatility = (
        daily_returns
        .rolling(window=window)
        .std()
    )

    return rolling_volatility

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0):

    sharpe_ratio = (
        daily_returns.mean()
        / daily_returns.std()
    ) * np.sqrt(252)  # Annualize the Sharpe ratio

    return sharpe_ratio

def calculate_max_drawdown(daily_returns):
 
    cumulative_returns = (
        1 + daily_returns
    ).cumprod()

    running_max = (
        cumulative_returns
        .cummax()
    )

    drawdown = (
        cumulative_returns - running_max
    ) / running_max

    max_drawdown = drawdown.min()

    return drawdown, max_drawdown