import numpy as np
import pandas as pd


def calculate_portfolio_metrics(returns):

    mean_return = returns.mean() * 252

    cov_metrics = returns.cov() * 252

    return mean_return, cov_metrics

# Monto Carlo 

def simulate_portfolios(
        returns, 
        tickers,
        num_portfolios=5000
):

    mean_return = returns.mean() * 252 

    cov_metrics = returns.cov() * 252

    portfolio_return = []

    portfolio_volatility = []

    portfolio_weights = []

    for i in range(num_portfolios):

        weights = np.random.random(len(tickers))

        weights = weights / np.sum(weights)

        portfolio_weights.append(weights)

        expected_return = np.sum(
            mean_return * weights
        )

        portfolio_return.append(expected_return)

        volatility = np.sqrt(
            weights.T
            @ cov_metrics
            @ weights
            )

        portfolio_volatility.append(volatility)

    return(
        portfolio_return,
        portfolio_volatility,
        portfolio_weights
    )


# Optimal Portfolio Function 

def find_optimal_portfolio(
        portfolio_return,
        portfolio_volatility,
        portfolio_weights,
        risk_free_rate=0.02
):

    efficient_frontier = pd.DataFrame({
        "Return": portfolio_return,
        "Risk": portfolio_volatility
    })

    efficient_frontier["Sharpe"] = (
        efficient_frontier["Return"]
        - risk_free_rate
    ) / efficient_frontier["Risk"]

    max_sharpe = (
        efficient_frontier["Sharpe"].idxmax()
    )

    optimal_sharpe = efficient_frontier.loc[
        max_sharpe,
        "Sharpe"
    ]

    optimal_return = efficient_frontier.loc[
        max_sharpe,
        "Return"
    ]

    optimal_risk = efficient_frontier.loc[
        max_sharpe,
        "Risk"
    ]

    optimal_weights = portfolio_weights[
        max_sharpe
    ]

    return(
        efficient_frontier,
        optimal_return, 
        optimal_risk,
        optimal_sharpe,
        optimal_weights
    )
