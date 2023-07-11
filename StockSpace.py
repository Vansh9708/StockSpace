from pandas_datareader import data

import pandas_datareader.data as web
import pandas as pd
import numpy as np

import datetime
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

start = datetime.datetime(2006,1,1)
end = datetime.datetime(2023,1,1)

# Bank of America
BAC = web.DataReader('BAC', 'stooq',start,end)
# CitiGroup
C = data.DataReader("C", 'stooq', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'stooq', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'stooq', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'stooq', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'stooq', start, end)

#American Express
AXP = data.DataReader("AXP",'stooq',start,end)

df = data.DataReader(['BAC','C','GS','JPM','MS','WFC','AXP'],'stooq',start,end)
tickers = ['BAC','C','GS','JPM','MS','WFC','AXP']
bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC,AXP],axis = 1 , keys =tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
bank_stocks.head()

bank_stocks.xs(key='Close',axis=1,level =1).max()
returns = pd.DataFrame()

for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()

sns.pairplot(returns[1:])

# Worst Drop (4 of them on Inauguration day)
returns.idxmin()


# Best Single Day Gain
# citigroup stock split in May 2011, but also JPM day after inauguration.
returns.idxmax()

returns.std()
# Citigroup riskiest #Amexx Less Riskiest

returns.loc['2022-01-01':'2022-12-31'].std()

sns.distplot(returns.loc['2022-01-01':'2022-12-31']['AXP Return'],color='green',bins=100
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()

for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

#Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
plt.figure(figsize=(12,6))
BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='AXP CLOSE')
plt.legend()
#Create a heatmap of the correlation between the stocks Close Price
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
