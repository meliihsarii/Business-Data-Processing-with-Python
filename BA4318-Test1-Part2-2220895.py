import pandas as pd


dfbrazil = pd.read_csv("sudeste.csv", delimiter=",", usecols= ['temp','date'])
dfbrazil['date'] = pd.to_datetime(dfbrazil['date'])


dfmadrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv", delimiter=",", skiprows=[i for i in range(1,1169)], usecols= ['Mean TemperatureC','CET'])
dfmadrid['CET'] = pd.to_datetime(dfmadrid['CET'])
dfmadrid.columns = ['date','Mean TemperatureC']


ts= pd.to_datetime('2015-01-01')
g= (dfbrazil.loc[(dfbrazil['date']) < ts]).groupby(['date'])
mean= g.mean()
rounded= mean.round(0)


dffinal=pd.merge(rounded,dfmadrid,on="date")
dffinal.columns=['Date','Brazil Temperature','Madrid Temperature']
print("Daily Average Temperature Brazil & Madrid:")
print(dffinal)

correlation= dffinal["Brazil Temperature"].corr(dffinal["Madrid Temperature"])

print("Correlation coefficient between dfbrazil&dfmadrid is:")
print(correlation)

#Interpretation of results #

# Correlation coefficient = -0.03065207,which is very close to zero.It shows a too weak negative relationship.
#In fact we can't clearly say a statistical correlation.
#In others, we can't explain Madrid's temperatures by Brazil's temperatures or vice versa.
# Melih Sarı-2220895