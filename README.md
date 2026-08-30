# :bar_chart: Finance AI Agent 

## Overview 

An interactive financial analytics appplication built with Python and Streamlit for analysing stocks, portfolio risk, diversification, simulation and portfolio optimization.

The project combines financial engineering concepts, quantitative analysis, Python programming, and interactive data visualisation to create a practical portfolio analytics application. 

--- 

## :dart: Project Objectives 

The main objectives of this projects are to:

- Analyse historical data stock proces and returns 
- Measure investment and portfolio risk 
- Analyse portfolio diversification 
- Construct portfolios using different asset weights 
- Simulate possible portfolio outcomes using Monte Carlo methods 
- Visualize the Efficient Frontier 
- Identify an optimal portfolio based on the Sharpe Ratio
- Generate rule-based financial insights 
- Apply financial engineering concepts in a practical Python application 

--- 

## :rocket: Features 

### :chart_with_upwards_trend: 1. Stock Analysis 

Users can select an individual stock and analyse:

- Historical closing prices 
- Daily Returns 
- Rolling Volatility 
- Maximum drawdown 
- Return distribution 
- Sharpe Ratio
- Summary return statistics

--- 

### 2. :bar_chart: Portfolio Analytics 

Users can select multiple stocks ad construct a portfolio 

The application provides:

- Portfolio stock prices 
- Portfolio weights 
- Portfolio allocation
- Portfolio volatility 
- Covariance matrix 
- Correlation heatmap 
- Monte Carlo portfolio simulation 
- Efficient Frontier 
- Optimal Portfolio Allocation 

--- 

### 3. :robot: AI Financial Insights 

The AI Insights section provides rule-based analysis of portfolio characteristics.

The system evaluates: 

- Risk-adjusted performance 
- Portfolio Volatility 
- Expected Returns 
- Portfolio diversification
- Portfolio concentration
- Optimal portfolio performance 

The application generates a **Portfolio Health Score out of 100** based on these portfolio characteristics.

> Note: The current AI Insights component is rule-based rather than a large language model (LLM). It uses predefined financial thresholds and portfolio metrics to generate insights. 

---

## :books: Financial Concepts 

#### Sharpe Ratio 

The Sharpe Ratio measures risk-adjusted performance. 

It compares the portfolio's excess return relative to its risk, measured by volatility.

A higher Sharpe Ratio generally indicates better risk-adjusted performance.

The project uses the Sharpe Ratio to identify the simulated portfolio with the strongest risk-adjusted performance. 

--- 

### Portfolio Volatility 

Portfolio volatility measures variation in portfolio returns. 

It is calculated using the portfolio weights and covariance matrix of asset return. 

Portfolio volatility is used as a measure of investment risk. 

---

### Correlation 

Correlation measures how closely the returns of two assets move relative to another. 

Lower correlations between assets can provide greater diversification benefits because the assets may not move in the same direction at the same.

--- 

### Maximum Drawdown 

Maximum drawdown measures the largest decline from a historical peak in portfolio value. 

It provides an indication of the potential downside experienced by an investment over the selected period. 

---

### :game_die: Monte Carlo Simulation 

Monte Carlo Simulation generates many possible portfolio outcomes using randomly generated inputs.  

In this prject, Monte Carlo Simulation is used to generate a large number of possible portfolios.

The process involves:

1. Generating random portfolio weights
2. Normalising the weights so that they sum to 100%
3. Calculating the expected portfolio return
4. Calculate portfolio volatility 
5. Repeating the process thousands of times
6. Comparing the simulated portfolios based on their risk and return characteristics

The project uses **500 simulated portfolios** when constructing the Efficient Frontier.

--- 

### :chart_with_upwards_trend: Efficient Frontier 

The Efficient Frontier represents portfolios that provide the best expected return for a given level of risk. 

The project uses Monte Carlo simulation to generate possible portfolios and visualize their risk-return charateristics.

The resulting risk-return distribution helps identify portfolios with attractive combinations is expected return and risk. 

--- 

### :dart: Optimal Portfolio 

The application identifies an optimal portfolio by finding the simulated portfolio with the highest Sharpe Ratio.

The resulting portfolio provides: 

- Expected Return 
- Portfolio risk 
- Sharpe Ratio 
- Asset allocation 

The optimal portfoli is selected from the simulated portfolios rather than from a closed-form optimisatiom algorithm.

--- 

## :brain: Portfolio Health Score 

The Portfolio Health Score is a rule-based scoring system out of 100 

| Metrics | Maximum Score |
|--- | --- |
| Sharpe Ratio | 25 |
| Portfolio Volatility | 25 | 
| Expected Return | 25 |
| Diverisification | 25 | 
| **Total** | **100** |

The score provides a simplified summary of the portfolio's overall charateristics.

The scoring system uses predefined thresholds to evaluate the portfolio's:

- Risk-adjusted performance 
- Risk level 
- Expected Return 
- Diversification 

---

### :hammer_and_wrench: Technologies Used 

- Python 
- Streamlit 
- Pandas 
- Numpy 
- Plotly 
- yFinance 
- Matplotlib 
- Seaborn 

---

## :open_file_folder: Project Structure 

```text
Finance_AI_Agent_Project/
│
├── app.py
├── requirements.txt
├── README.md
│
└── src/
    ├── portfolio_analysis.py
    ├── risk_metrics.py
    └── ai_insights.py


