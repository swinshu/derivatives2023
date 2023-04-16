import yfinance as yf
from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame

def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))

def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

def bs_call(S,K,T,r,sigma):
    """
    Black-Scholes on call options. Returns price of the option.
    """
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
def bs_put(S,K,T,r,sigma):
    """
    Black-Scholes on put options. Returns price of the option.
    """
    return K*exp(-r*T)-S*bs_call(S,K,T,r,sigma)

tickers_list = ["ita", "rtx", "ba", "lmt", "gd","noc"] # defense and aerospace

ita = yf.Ticker("ITA").options

# pick a monthly expiration 
def 

# Calculate delta of total position looking at iv and strike for option positions and the number of shares owned by the portfolio.
def call_delta(S,K,T,r,sigma):
    return norm.cdf(d1(S,K,T,r,sigma))

def put_delta(S,K,T,r,sigma):
    return -norm.cdf(-d1(S,K,T,r,sigma))

# sigma = np.sqrt(252) * df['returns'].std()
