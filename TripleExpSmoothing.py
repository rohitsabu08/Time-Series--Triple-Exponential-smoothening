#importing the libraries:
import numpy as np
from pandas import read_csv
from matplotlib import pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error 
from math import sqrt 
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#Reading the dataset (sales dataset of shampoo for every month)
series = read_csv('shampoosales.csv')
train = series.iloc[0:30]       #Splitting the test and train dataset
test = series.iloc[30:]

# plot the full series and analysing the seasonality:
plt.plot(series['Sales'],label='series')   
plt.show()
sm.tsa.seasonal_decompose(train.Sales, model='add', freq=4).plot()
plt.show()

# Using the Triple ExponentialSmoothing
model = ExponentialSmoothing(np.asarray(train['Sales']), 
                             seasonal_periods=4, trend="mul", seasonal='add')
fit1 = model.fit( optimized=True)            #fitting the model
test['TES_add'] = fit1.forecast(len(test))   #Appending the forecast
#Plotting the existing and the DES forecast
plt.plot(train['Sales'], label='train dataset')
plt.plot(test['Sales'], label='test dataset')
plt.plot(test['TES_add'], label='TES forecast')
plt.legend(loc='best')
plt.show()
#Printing the forecast and RMSE values:
print(test)
rmse=sqrt(mean_squared_error(test.Sales, test['TES_add']))
print("The RMSE of the model is:",rmse)

