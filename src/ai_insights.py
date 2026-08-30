def calculate_health_score(
        optimal_sharpe,
        optimal_risk,
        average_corr, 
        optimal_return
):

    score = 0

    # Sharpe Ratio
    if optimal_sharpe >= 1:
        score += 25 
    elif optimal_sharpe >= 0.5:
        score += 15
    else:
        score += 5 

    # Risk (Volatility)
    if optimal_risk < 0.15:
        score += 25 
    elif optimal_risk < 0.25:
        score += 15
    else:
        score += 5 

    # Average Correlation
    if average_corr < 0.60:
        score += 25 
    elif average_corr < 0.80:
        score += 15
    else:
        score += 5 

    # Return
    if optimal_return > 0.15:
        score += 25
    elif optimal_return > 0.08:
        score += 15 
    else:
        score += 5 

    return score

def analyze_sharpe_ratio(optimal_sharpe):

    if optimal_sharpe >= 1:
        return "Excellent risk-adjusted performance."
    
    elif optimal_sharpe >= 0.5:
        return "Moderate risk-adjusted performance."
    
    else:
        return "Risk-adjusted performance is relatively low."

def analyze_risk(optimal_risk):

    if optimal_risk < 0.15:
        return "The portfolio has relatively low volatility."

    elif optimal_risk < 0.25:
        return "The portfolio has moderate volatility."

    else:
        return "The portfolio has high volatility."

def analyze_diversification(average_corr):

    if average_corr < 0.60:
        return "The assets are reasonably diversified."

    elif average_corr < 0.80:
        return "The portfolio has moderate diversification."

    else:
        return "Many assets in the portfolio are highly correlated, indicating poor diversification."

def analyze_return(optimal_return):

    if optimal_return > 0.15:
        return "The optimized portfolio has a strong expected return."

    elif optimal_return > 0.08:
        return "The optimized portfolio has a moderate expected return."

    else:
        return "The optimized portfolio has a low expected return."