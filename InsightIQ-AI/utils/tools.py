import time
import requests
import yfinance as yf
from functools import wraps
from typing import Any, Callable, Dict, Union
from langchain.tools import tool

from MarketInsight.utils.logger import get_logger

logger = get_logger("Tools")


def _tool_monitor(func: Callable) -> Callable:
    """
    Decorator to abstract input validation, performance timing, 
    logging, and exception handling for all financial tools.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        target = kwargs.get('ticker') or kwargs.get('company_name')
        if not target and args:
            target = args[0]
            
        if not target or not isinstance(target, str):
            return "Error: Invalid identifier provided. Please provide a valid ticker or company name."

        logger.info(f"Executing {func.__name__} for target: {target}")
        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            
            # Catch None or empty dicts/dataframes safely
            if result is None or (isinstance(result, dict) and not result):
                return f"No data available for {target}."

            elapsed_time = time.time() - start_time
            logger.info(f"Successfully executed {func.__name__} for {target} in {elapsed_time:.3f}s")
            return result

        except Exception as e:
            logger.error(f"Error in {func.__name__} for {target}: {str(e)}", exc_info=True)
            return "Error: Failed to process the financial request. Please try again later."
            
    return wrapper


@tool('get_stock_price', description="A function that returns the current stock price of a given ticker")
@_tool_monitor
def get_stock_price(ticker: str) -> Union[float, str]:
    info = yf.Ticker(ticker).info
    return info.get('currentPrice') or info.get('regularMarketPrice')


@tool('get_historical_data', description="A function that returns the historical data of a given ticker in the given start and end date")
@_tool_monitor
def get_historical_data(ticker: str, start_date: str, end_date: str) -> dict:
    return yf.Ticker(ticker).history(start=start_date, end=end_date).to_dict()


@tool('get_stock_news', description="A function that returns the news of a given ticker")
@_tool_monitor
def get_stock_news(ticker: str) -> list:
    return yf.Ticker(ticker).news


@tool('get_balance_sheet', description="A function that returns the balance sheet of a given ticker")
@_tool_monitor
def get_balance_sheet(ticker: str) -> dict:
    return yf.Ticker(ticker).balance_sheet.to_dict()


@tool('get_income_statement', description="A function that returns the income statement of a given ticker")
@_tool_monitor
def get_income_statement(ticker: str) -> dict:
    return yf.Ticker(ticker).financials.to_dict()


@tool('get_cash_flow', description="A function that returns the cash flow statement of a given ticker")
@_tool_monitor
def get_cash_flow(ticker: str) -> dict:
    return yf.Ticker(ticker).cashflow.to_dict()


@tool('get_company_info', description="A function that returns company profile and key financial ratios")
@_tool_monitor
def get_company_info(ticker: str) -> dict:
    return yf.Ticker(ticker).info


@tool('get_dividends', description="A function that returns the dividend payment history of a given ticker")
@_tool_monitor
def get_dividends(ticker: str) -> dict:
    return yf.Ticker(ticker).dividends.to_dict()


@tool('get_splits', description="A function that returns the stock split history of a given ticker")
@_tool_monitor
def get_splits(ticker: str) -> dict:
    return yf.Ticker(ticker).splits.to_dict()


@tool('get_institutional_holders', description="A function that returns the institutional ownership data of a given ticker")
@_tool_monitor
def get_institutional_holders(ticker: str) -> dict:
    return yf.Ticker(ticker).institutional_holders.to_dict()


@tool('get_major_shareholders', description="A function that returns the major share holder data of a given ticker")
@_tool_monitor
def get_major_shareholders(ticker: str) -> dict:
    return yf.Ticker(ticker).major_holders.to_dict()


@tool('get_mutual_fund_holders', description="A function that returns the mutual fund ownership data of a given ticker")
@_tool_monitor
def get_mutual_fund_holders(ticker: str) -> dict:
    return yf.Ticker(ticker).mutualfund_holders.to_dict()


@tool('get_insider_transactions', description="A function that returns the insider buy/sell transactions of a given ticker")
@_tool_monitor
def get_insider_transactions(ticker: str) -> dict:
    return yf.Ticker(ticker).insider_transactions.to_dict()


@tool('get_analyst_recommendations', description="A function that returns the analyst recommendations of a given ticker")
@_tool_monitor
def get_analyst_recommendations(ticker: str) -> dict:
    return yf.Ticker(ticker).recommendations.to_dict()


@tool('get_analyst_recommendations_summary', description="A function that returns the analyst recommendations summary of a given ticker")
@_tool_monitor
def get_analyst_recommendations_summary(ticker: str) -> dict:
    return yf.Ticker(ticker).recommendations_summary.to_dict()


@tool('get_ticker', description="A function that returns the ticker/symbol of a given company")
@_tool_monitor
def get_ticker(company_name: str) -> str:
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={company_name}"
    
    # Required to prevent 403 Forbidden errors from Yahoo Finance
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    if data.get('quotes') and len(data['quotes']) > 0:
        return data['quotes'][0]['symbol']
    
    return f"No ticker symbol found for {company_name}"
