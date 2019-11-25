import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import matplotlib.pylab as plt
from statsmodels.tsa.stattools import adfuller

df_brazil = pd.read_csv("sudeste.csv", usecols=["date", "temp"])
df_madrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv", usecols=["CET", "Mean TemperatureC"])


def prepare_brazil(df):
    temp = df.groupby("date").mean().reset_index()
    date_series = temp["date"]
    temp_series = temp["temp"]
    temp_series.index =  pd.DatetimeIndex(date_series)

    start_date, end_date = date_series.head(1).values[0], date_series.tail(1).values[0]
    date_indx = pd.date_range(start_date, end_date)
    result = temp_series.reindex(date_indx, fill_value=0)

    return result

def prepare_madrid(df):
    temp = df
    date_series = temp["CET"]
    temp_series = temp["Mean TemperatureC"]
    temp_series.index =  pd.DatetimeIndex(date_series)

    start_date, end_date = date_series.head(1).values[0], date_series.tail(1).values[0]
    date_indx = pd.date_range(start_date, end_date)
    result = temp_series.reindex(date_indx, fill_value=0)

    return result


brazil,madrid = prepare_brazil(df_brazil), prepare_madrid(df_madrid)

plt.plot(brazil)
plt.title("brazil")
plt.show()
plt.plot(madrid)
plt.title("madrid")
plt.show()

print("adfuller test of brazil")
print(adfuller(brazil.dropna()))
print("adfuller test of madrid")
print(adfuller(madrid.dropna()))

plt.hist(brazil.dropna())
plt.title("histogram of brazil")
plt.show()

plt.hist(madrid.dropna())
plt.title("histogram of madrid")
plt.show()

X = madrid.dropna().values
low, high = X[:len(X)//2], X[len(X)//2:]
print ("Madrid's low mean is ", low.mean(), "and high mean is", high.mean())
print ("Madrid's low variation is ", low.var(), "and high variation is", high.var())

X = brazil.values
low, high = X[:len(X)//2], X[len(X)//2:]
print ("Brazil's low mean is", low.mean(), "and high mean is", high.mean())
print ("Brazil's low variation is", (low.var()), "and high variation is", (high.var()))
lag_plot(brazil)

plt.title("Lag plot of Brazil")
plt.show()
lag_plot(madrid)
plt.title("Lag plot of Madrid")
plt.show()

autocorrelation_plot(brazil)
plt.title("Autocorrelation of Brazil")
plt.show()
autocorrelation_plot(madrid)
plt.title("Autocorrelation of Madrid")
plt.show()

#We can conclude that there is no increasing trends in temperature datasets
#We observed that Brazil's and Madrid's temperature datasets are both stationary regarding as autocorrelation,plots,lag and histogram.
#Also, according to Augmented Dickey-Fuller test , we reject the null hypothesis in Brazil and Madrid since p-values are smaller than 0.05.
#As a result,we can say that there is global warming both in Madrid and Brazil
#MELİH SARI-2220895