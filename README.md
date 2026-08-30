# :bar_chart: Finance AI Agent 

## Overview 

Finance AI Agent is an interactive financial analytics application built with Python and Streamlit.

The application allows users to analyse individual stocks, construct portfolio risk, simulate possible portfolio outcomes, identify optimal portfolio allocations, and generate rule-based financial insights. 

The project combines financial engineering concepts with python programming and interactive data visualization.

--- 

## :dart: Project Objectives 

The main objectives of this projects are to:

- Analyse historical data stock proces and returns 
- Measure investment risk 
- Analyse portfolio diversification 
- Construct portfolios using different asset weights 
- Simulate random portfolios using Monte Carlo methods 
- Visualize the Efficient Frontier 
- Identify an optimal portfolio based on the Sharpe Ratio
- Generate rule-based portfolio insights 
- Apply financial engineering concepts in a practical Python application 

--- 

## :rocket: Features 

### 1. Stock Analysis 

Users can select an individual stock and analyse:

- Historical closing prices 
- Daily Returns 
- Rolling Volatility 
- Maximum drawdown 
- Return distribution 
- Sharpe Ratio
- Summary return statistics

--- 

### 2. Portfolio Analytics 

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

### 3. Financial Insights 

The AI Insights section provides rule-based analyis of portfolio characteristics.

The system evaluates: 

- Risk-adjusted performance 
- Portfolio Volatility 
- Expected Returns 
- Portfolio concentration
- Optimal portfolio performance 

The application generates a Portfolio Health Score out of 100 based on those metrics 

---

## :upwards_trends: Financial Concepts 

#### Sharpe Ratio 

The Sharpe Ratio measure risk-adjusted performance. 

It compare the portfolio's excess return to its volatility 

A higher Sharpe Ratio generally indicates better risk-adjusted performance.

--- 

### Portfolio Volatility 

Portfolio Volatility measures the amount of variation in portfolio returns. 

It is calculated using the portfolio weights and covariance matrix of asset return. 

---

### Correlation 

Correlation measures how closely two assets move relative to another. 

Lower correaltions cane provide greater diversification benefits.

--- 

### Maximum Drawdown 

Maximum drawdown measures the largest decline from a historical peak in portfolio value. 

It provides an indication of the potential downside experienced by an investment. 

---

### Monte Carlo Simulation 

Monte Carlo Simulation generates many possible outcomes by randomly generating portfolio weights or return paths. 

In this prject, Monte Carlo Simulation is used to: 

1. Generate random portfolio weights
2. Calculate expected portfoloio returns
3. Calculate portfolio volatility 
4. Generate a large number of possible portfolios
5. Identify portfolios with difereny risk-return

--- 

### Efficient Frontier 

The Efficient Frontier represents portfolio that provides the best expected return for a given level of risk. 

The project uses Monte Carlo simulation to generate possible portfolios and visualise their risk-return charateristics.

--- 

### Optimal Portfolio 

The application identifies an optimal portfolio by finding the simulation portfolio with the highest Sharpe Ration 

The resulting portfolio provides: 

- Expected Return 
- Expected risk 
- Sharpe Ration 
- Asset allocation 

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

The score provides a simple summary of the portfolio's overall charateristics.

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


