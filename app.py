import streamlit as st
import yfinance as yf
from datetime import date 
import plotly.express as px 
import matplotlib.pyplot as plt 
from matplotlib.ticker import PercentFormatter 
import numpy as np 
import pandas as pd
import seaborn as sns 

# Import Functions from portfolio_analysis.py and risk_metrics.py

from src.portfolio_analysis import (
    calculate_portfolio_metrics,
    simulate_portfolios,
    find_optimal_portfolio
)

from src.risk_metrics import (
    calculate_daily_returns,
    calculate_rolling_volatility,
    calculate_sharpe_ratio, 
    calculate_max_drawdown
)

from src.ai_insights import (
    calculate_health_score,
    analyze_sharpe_ratio,
    analyze_risk,
    analyze_diversification,
    analyze_return
)

#Page Configuration 

st.set_page_config(
    page_title="Financial Ai Agent",
    page_icon=":chart_with_upwards_trend:", 
    layout="wide"
)

st.title(":chart_with_upwards_trend: Financial AI Agent")

#Sidebar 

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Stock Analysis",
        "Portfolio Analytics",
        "AI Insights",
    ]
)

if page == "Home":

    st.header("Welcome")

    st.write(
        "**This Finance AI Agent provides an interactive financial analytics using Python and Streamlit**"
    )

elif page == "Stock Analysis":

    st.header("Stock Analysis")

    ticker = st.selectbox(
        "Select a Company",
        [
            "AAPL",
            "MSFT",
            "AMZN",
            "GOOG",
            "TSLA",
            "META",
            "NVDA"
        ]
    )

    start_date = st.date_input(
        "Start_Date",
        value=date(2022, 1, 1)
    )

    end_date = st.date_input(
        "End_Date",
        value=date.today()
    )

    data = yf.download(
        ticker, 
        start=start_date,
        end=end_date
    )

    ### st.write(data.columns) - debugging to see exactly what yfinance downloaded

    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    with st.expander("📋 View Raw Stock Data"):
        st.dataframe(
        data,
        use_container_width=True
    )

    #### Financial Calculation

 # Daily Returns 
    data["Daily Returns"] = calculate_daily_returns(
        data["Close"]
    )
    
    data["Daily Returns (%)"] = (
        data["Daily Returns"] * 100
    )

    with st.expander("📊 View Daily Returns Data"):
        st.dataframe(
                data[["Close", "Daily Returns (%)"]],
                use_container_width=True
            )

 # Rolling Vol 
    data["Rolling Volatilities (%)"] = (
        calculate_rolling_volatility(
            data["Daily Returns (%)"]
        )
    )

    with st.expander("📊 View Rolling Volatilities Data"):
        st.dataframe(
            data[["Daily Returns (%)", "Rolling Volatilities (%)"]],
            use_container_width=True
        )

 # Annualize Sharpe Ratio
    sharpe_ratio = calculate_sharpe_ratio(
        data["Daily Returns"]
    )
    
 # Return Distribution 
    mean_return = data["Daily Returns (%)"].mean()

 # Cummulative Returns 

    data["Drawdown"], max_drawdown = (
        calculate_max_drawdown(
            data["Daily Returns"]
        )
    )

 ## Tabs

    tab1, tab2, tab3 = st.tabs(
        ["📈 Price Analysis", "📊 Risk Analysis", "📋 Statistics"]
    )
        
    with tab1:

        st.subheader("Price Analysis")

        st.subheader(f"{ticker} Stock Data")

     #Latest Price Metrics
    
        col1, col2, col3, col4 = st.columns(4)
    
        latest = data["Close"].iloc[-1]
        highest = data["High"].max()
        lowest = data["Low"].min()
        average = data["Open"].mean()
    
        col1.metric("Latest Price", f"${latest:.2f}")
        col2.metric("Highest Price", f"${highest:.2f}")
        col3.metric("Lowest Price", f"${lowest:.2f}")
        col4.metric("Average Price", f"${average:.2f}")

        # Daily Price Chart

        plt = px.line(
            data,
            x=data.index,
            y="Close",
            title=f"{ticker} Closing Prices"
        )

        plt.update_layout(
            xaxis_title="Date",
            yaxis_title="Daily Prices ($USD)"
        )
        
        st.plotly_chart(plt, use_container_width=True)
        
    with tab2:

        st.subheader("Risk Analysis")

        # Daily Returns 

        fig = px.line(
            data,
            x=data.index,
            y="Daily Returns (%)",
            title=f"{ticker} Daily Returns"
            )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Daily Returns (%)"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Rolling Volatility 

        st.subheader("21-Day Rolling Volatility")

        fig = px.line(
            data,
            x=data.index,
            y="Rolling Volatilities (%)", 
            title=f"{ticker} 21-Day Rolling Volatility"
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Volatility (%)"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Maximum Drawdown 
    
        st.subheader("Maximum Drawdown")
    
        st.metric(
            "Maximum Drawdown",
            f"{max_drawdown:.2%}"
        )
    
        fig = px.line(
            data,
            x=data.index,
            y="Drawdown",
            title=f"{ticker} Drawdown"
        )
    
        st.plotly_chart(fig, use_container_width=True)
        
            
    with tab3:

        st.subheader("Statistics")

        # Return Distribution
       
        st.subheader("Return Distribution")
        
        fig = px.histogram(
            data,
            x="Daily Returns (%)",
            nbins=50,
            title=f"{ticker} Daily Return Distribution"
        )
        
        fig.add_vline(
            x=mean_return,
            line_dash="dash",
            line_color="red",
            annotation_text="Mean"
        )
        
        st.plotly_chart(fig, use_container_width=True)

        # Sharpe Ratio 
        
        st.subheader("Sharpe Ratio")
        
        st.metric(
            "Annualized Sharpe Ratio",
            f"{sharpe_ratio:.2f}"
        )
    
        # Summary Statistics 

        st.subheader("Return Statistics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Mean Return (%)",
            f"{data['Daily Returns (%)'].mean():.2f}"
        )

        col2.metric(
            "Median Return (%)",
            f"{data['Daily Returns (%)'].median():.2f}"
        )

        col3.metric(
            "Minimum Return (%)",
            f"{data['Daily Returns (%)'].min():.2f}"
        )

        col4.metric(
            "Maximum Return (%)",
            f"{data['Daily Returns (%)'].max():.2f}"
        )

elif page == "Portfolio Analytics":

    st.header(":chart_with_upwards_trend: Portfolio Analytics")

    #Select stocks 

    tickers = st.multiselect(
        "Select Stocks",
        [
            "AAPL",
            "MSFT",
            "AMZN",
            "GOOG",
            "META",
            "NVDA",
            "TSLA"
        ],
        default=["AAPL", "MSFT"]
    )

    # Select date

    start_date = st.date_input(
        "Start Date",
        value=date(2022, 1, 1)
    )

    end_date = st.date_input(
        "End Date",
        value=date.today()
    )

    if not tickers:
        st.warning("Please select at least one stock")
        st.stop()

    m_portfolio = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )

    # Closing Price 
    
    prices = m_portfolio["Close"]

    st.subheader("Portfolio Prices")

    #Display Data 
    with st.expander("📋 View Raw Stock Data"):
        st.dataframe(prices)

    tab1, tab2, tab3 = st.tabs(
            ["📈 Portfolio", "📊 Risk", "⚙️ Optimization"]
        )
    with tab1: 

        fig = px.line(
            prices, 
            x=prices.index,
            y=prices.columns,
            title="Portfolio Stock Prices"
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Daily Prices ($USD)"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Portfolio Weights

        st.subheader("Portfolio Weights")

        weights = []

        for ticker in tickers:
            weight = st.slider(
                f"{ticker} Weights (%)",
                min_value=0,
                max_value=100,
                value=int(100 / len(tickers))
            )

            weights.append(weight)

        weights = np.array(weights) / 100

        total_weights = weights.sum()

        # Display 
        st.write(f"Total Weights: {total_weights:.2f}")

        # Vaildate Weights 

        if abs(total_weights - 1) > 0.01:
            st.error("Portfolio weights must add up to 100%")
            st.stop()

        #Show the Portfolio Allocation

        weights_fd = pd.DataFrame({
            "Ticker": tickers,
            "Weight": weights
        })

        st.dataframe(weights_fd)

        #Plot Pie Chart

        fig = px.pie(
            weights_fd,
            names="Ticker",
            values="Weight",
            title="Portfolio Allocation"
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab2:

        # Portfolio Volatility

        returns = prices.pct_change().dropna()

        #Annualized Covariance metrix 

        cov_met = returns.cov() * 252

        portf_vol = np.sqrt(
            weights.T @ cov_met @ weights
        )

        # Display Results 
        st.subheader("Portfolio Volatility")

        st.metric(
            "Annualized Volatility",
            f"{portf_vol:.2%}"
        )

        st.header("Covariance Matrix")

        with st.expander("📐 View Covariance Matrix"):
            st.dataframe(
            cov_met,
            use_container_width=True
        )

        ##Correlation Heatmap 

        corr_matrix = returns.corr()

        st.subheader("Correlation Heatmap")

        fig = px.imshow(
            corr_matrix,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            aspect="auto",
            title="Stock Correlation Matrix"
        )

        fig.update_layout(
            xaxis_title="Stocks",
            yaxis_title="Stocks"
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        # Portfolio Daily Returns 

        portfolio_rets = returns @ weights 

        mean_rets = portfolio_rets.mean()

        volatility_rets = portfolio_rets.std()

        # Simulation Settings 

        number_sim = 100

        number_days = 252

        # Run Simulation 

        sim_df = pd.DataFrame()

        for i in range(number_sim):

            sim_rets = np.random.normal(
                mean_rets,
                volatility_rets,
                number_days
            )

            sim_prices = (1 + sim_rets).cumprod()

            sim_df[i] = sim_prices

        st.write("Number of simulations:", len(sim_df.columns))
        st.write("Simulation shape:", sim_df.shape)

        #Plot line graph 

        fig = px.line(
            sim_df,
            title="Monte Carlo Portfolio Simulation"
        )

        fig.update_layout(
            xaxis_title="Trading Days",
            yaxis_title="Portfolio Value"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            The Monte Carlo simulation shows possible future portfolio
            values based on historical average returns and volatility.
            Each line represents one possible future path.
            """
        )

        #Efficient Frontier 
        #Portfolio Metrucs 

        mean_return, cov_metrics = calculate_portfolio_metrics(
            returns
        )

        ##Monte Carlo Simulation for Efficient Frontier
        ## Simulate Random Portfolios
    
        portfolio_return, portfolio_volatility, portfolio_weights = (
            simulate_portfolios(
                returns,
                tickers,
                num_portfolios=5000
            )
        )

        ## Optimal Portfolio 

        (
            efficient_frontier,
            optimal_return,
            optimal_risk,
            optimal_sharpe,
            optimal_weights
        ) = find_optimal_portfolio(
            portfolio_return,
            portfolio_volatility,
            portfolio_weights
        )

        fig = px.scatter(
            efficient_frontier,
            x="Risk",
            y="Return",
            color="Sharpe", 
            color_continuous_scale="Viridis",
            title="Efficient Frontier"
        )

            ## Highlight Optimal Portfolio 

        fig.add_scatter(
            x=[optimal_risk],
            y=[optimal_return],
            mode="markers",
            marker=dict(
                color="red",
                size=14,
                symbol="star"
            ),
            name="Maximum Sharpe Ratio"
        )

        st.plotly_chart(fig, use_container_width=True)

        ## Optimal Portfolio allocation

        st.subheader("Optimal Portfolio")

        optimal_df = pd.DataFrame({
            "Ticker": tickers,
            "Weights": optimal_weights
        })

        st.dataframe(optimal_df)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Expected Returns",
            f"{optimal_return:.2%}"
        )

        col2.metric(
            "Volatility",
            f"{optimal_risk:.2%}"
        )

        col3.metric(
            "Sharpe Ratio",
            f"{optimal_sharpe:.2f}"
        )

elif page == "AI Insights":


    st.header("🤖 AI Financial Insights")
    
    st.write(
        "This section automatically analyzes the portfolio and "
        "provides investment insights based on the calculated metrics."
    )
    
        # SELECT STOCKS
    
    tickers = st.multiselect(
        "Select Stocks",
        [
            "AAPL",
            "MSFT",
            "AMZN",
            "GOOG",
            "META",
            "NVDA",
            "TSLA"
        ],
        default=["AAPL", "MSFT"]
    )
    
       
        ## SELECT DATE
        
    start_date = st.date_input(
        "Start Date",
        value=date(2022, 1, 1)
    )
    
    end_date = st.date_input(
        "End Date",
        value=date.today()
    )
    
        ## Ensure that least one stock is selected
    
    if not tickers:
        st.warning("Please select at least one stock")
        st.stop()
    
        ## DOWNLOAD DATA
    
    m_portfolio = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )

        ## CLOSING PRICES
    
    prices = m_portfolio["Close"]
    
    st.subheader("📊 Portfolio Price Data")

    with st.expander("📋 View Raw Stock Data"):    
        st.dataframe(prices,
                     use_container_width=True
        )

    ## Returns 

    returns = prices.pct_change().dropna()

    # Annualized returns and covariance
    
    mean_return = returns.mean() * 252
    
    cov_metrics = returns.cov() * 252 
    
    ##Create a List 
    
    portfolio_returns = []
    
    portfolio_volatility = []
    
    portfolio_weights = []
    
    num_portfolio = 5000
    
        ## Simulate Random Portfolios
        
    for i in range(num_portfolio):
    
        weights_rp = np.random.random(len(tickers))
    
        weights_rp = weights_rp / np.sum(weights_rp)
    
        portfolio_weights.append(weights_rp)

        ## Expected portfolio returns 
    
        expected_return = np.sum(
            mean_return * weights_rp
        )
    
        portfolio_returns.append(expected_return)

        ##Portfolio Volatilty 
    
        volatility = np.sqrt(
            weights_rp.T 
            @ cov_metrics
            @ weights_rp
        )
    
        portfolio_volatility.append(volatility)
    
    ## Efficient Frontier 
    
    efficient_frontier = pd.DataFrame({
        "Return": portfolio_returns,
        "Risk": portfolio_volatility
    })

    ## Sharpe Ratio
    
    risk_free_rate = 0.02
    
    efficient_frontier["Sharpe"] = (
        efficient_frontier["Return"] 
        - risk_free_rate
        ) / efficient_frontier["Risk"]

    ### Optimal Allocation
    
    max_sharpe = efficient_frontier["Sharpe"].idxmax()

    optimal_sharpe = efficient_frontier.loc[max_sharpe, "Sharpe"]

    optimal_return = efficient_frontier.loc[max_sharpe, 'Return']

    optimal_risk = efficient_frontier.loc[max_sharpe, 'Risk']

    ###Average Correlation 

    corr_matrix = returns.corr()

    upper_triangle = corr_matrix.where(
        np.triu(
            np.ones(corr_matrix.shape),
            k=1
        ).astype(bool)
    )

    average_corr = upper_triangle.stack().mean()

    ## Handle the case where only one stock is selected

    if np.isnan(average_corr):
        average_corr = 0
        
    score = calculate_health_score(
        optimal_sharpe,
        optimal_risk,
        average_corr,
        optimal_return
    )

    #Display Portfolio Health Score 

    st.subheader(":trophy: Portfolio Health Score")

    st.metric(
        "Portfolio Health Score",
        f"{score}/100"
    )

    ## Sharpe Analysis 
    st.header(":chart_with_upwards_trend: Sharpe Ratio Analysis")

    sharpe_message = analyze_sharpe_ratio(
        optimal_sharpe
    )

    if optimal_sharpe > 1:

        st.success(
            f"{sharpe_message} "
            f"Sharpe Ratio: {optimal_sharpe:.2f}"
        )

    elif optimal_sharpe > 0.5:

        st.warning(
            f"{sharpe_message} "
            f"Sharpe Ratio: {optimal_sharpe:.2f}"
        )

    else:

        st.error(
            f"{sharpe_message} "
            f"Sharpe Ratio: {optimal_sharpe:.2f}"
        )

    ###  Risk Analysis

    st.subheader("Portfolio Risk")

    risk_message = analyze_risk(optimal_risk)

    if optimal_risk < 0.15:

        st.success(
            f"{risk_message} "
            f"Volatility: {optimal_risk:.2%}"
        )

    elif optimal_risk < 0.25:

        st.info(
            f"{risk_message} "
            f"Volatility: {optimal_risk:.2%}"
        )

    else:

        st.warning(
            f"{risk_message} "
            f"Volatility: {optimal_risk:.2%}"
        )

    #Diversification Analysis

    st.header(":chart_with_upwards_trend: Diversification")

    if len(tickers) == 1:

        st.info(
            "Only one stock has been selected."
            "Diversification cannot be assessed"
        )

    else:

        diversification_message = analyze_diversification(
            average_corr
        )

        if average_corr < 0.60:

            st.success(
                f"{diversification_message} "
                f"Average Correlation: {average_corr:.2f}"
            )

        elif average_corr < 0.80:

            st.info(
                f"{diversification_message} "
                f"Average Correlation: {average_corr:.2f}"
            )
        else:

            st.warning(
                f"{diversification_message} "
                f"Average Correlation: {average_corr:.2f}"
            )

    # Expected Returns Analysis

    st.header(":chart_with_upwards_trend: Expected Portfolio Return")

    return_message = analyze_return(
        optimal_return
    )

    if optimal_return > 0.15:

        st.success(
            f"{return_message} "
            f"Expected annual return: {optimal_return:.2%}"
        )

    elif optimal_return > 0.08:

        st.info(
            f"{return_message} "
            f"Expected annual return: {optimal_return:.2%}"
        )

    else:

        st.warning(
            f"{return_message} "
            f"Expected annual return: {optimal_return:.2%}"
        )

    ## Optimal Portfoilo Analysis

    st.header(" :dart: Optimal Portfoilo Analysis")

    optimal_message = analyze_sharpe_ratio(
        optimal_sharpe
    )

    st.write(
        f"""

        **Expected Return:** {optimal_return:.2%}

        **Portfolio Risk:** {optimal_risk:.2%}

        **Sharpe Ratio:** {optimal_sharpe:.2f}
        """
        )

    if optimal_sharpe > 1:

        st.success(optimal_message)

    elif optimal_sharpe > 0.5:

        st.info(optimal_message)

    else:
        
        st.warning(optimal_message)
    
    ## Actual Allocation 

    st.subheader("Optimal Portfolio Allocation")

    optimal_weights = portfolio_weights[max_sharpe]
    
    optimal_df = pd.DataFrame({
            "Ticker": tickers,
            "Weight": optimal_weights
    })

    optimal_df["Weight (%)"] = (
        optimal_df["Weight"] * 100 
    )

    st.dataframe(
        optimal_df[
            ["Ticker", "Weight (%)"]
        ],
        hide_index=True
    )

    fig = px.pie(
        optimal_df,
        names="Ticker",
        values="Weight (%)",
        title="Optimal Portfolio Allocation"
    )

    st.plotly_chart(fig, use_container_width=True)

    ## Concentration Analysis

    st.subheader(" :pushpin: Concentration Analysis")

    largest_weights = optimal_weights.max()

    largest_stock = tickers[
        np.argmax(optimal_weights)
    ]

    ###

    if largest_weights > 0.40:

        st.warning(
            f"The optimized portfolio is highly concentrated in "
            f"{largest_stock}, with an allocation of "
            f"{largest_weights:.2%}"
        )

    elif largest_weights > 0.25:

        st.info(
            f"{largest_stock} has the largest allocation at "
            f"{largest_weights:.2%}. The portfolio has some "
            f"The portfolio has some concentration risk."
        )

    else:

        st.success(
            f"The portfolio is relatively well distributed, with "
            f"the largest allocation being {largest_stock} at "
            f"{largest_weights: .2%}"
        )

