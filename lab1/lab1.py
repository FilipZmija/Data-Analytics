import pandas as pd
from matplotlib import figure, pyplot as plt
import numpy 
import cmdstanpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

df = pd.read_csv("Data1.csv", index_col=0)
print(df.head())

'''data plot'''
df.plot(subplots=True, layout=(6, 1))
plt.show()

'''histogram'''
histo = plt.figure(1)
plt1 = histo.add_subplot(611)
plt2 = histo.add_subplot(612)
plt3 = histo.add_subplot(613)
plt4 = histo.add_subplot(614)
plt5 = histo.add_subplot(615)
plt6 = histo.add_subplot(616)

plt1.hist(df['theta_1'], bins=10)
plt2.hist(df['theta_2'])
plt3.hist(df['theta_3'])
plt4.hist(df['theta_4'], bins=30)
plt5.hist(df['theta_5'])
plt6.hist(df['theta_6'])
plt.show()

df['theta_1'].plot.kde()
plt.show()
df['theta_2'].plot.kde()
plt.show()
df['theta_3'].plot.kde()
plt.show()
df['theta_4'].plot.kde()
plt.show()
df['theta_5'].plot.kde()
plt.show()
df['theta_6'].plot.kde()
plt.show()

df1 = pd.read_csv("Data1.csv")
df1 = df1.drop(columns=['theta_6', 'theta_5'])
df1 = df1.rename(columns={'Unnamed: 0': "Date"})
df1['Date']= pd.to_datetime(df1['Date']) 
df1 = df1[df1['Date'].dt.year == 2018]
df2 = df1.set_index('Date')
print(df2.head())

df2.plot(subplots=True, layout=(4, 1))
histoo = plt.figure(3)
plt11 = histoo.add_subplot(411)
plt22 = histoo.add_subplot(412)
plt33 = histoo.add_subplot(413)
plt44 = histoo.add_subplot(414)

plt11.hist(df['theta_1'], bins=10)
plt22.hist(df['theta_2'])
plt33.hist(df['theta_3'])
plt44.hist(df['theta_4'])
plt.show()

df['theta_1'].plot.kde()
plt.show()
df['theta_2'].plot.kde()
plt.show()
df['theta_3'].plot.kde()
plt.show()
df['theta_4'].plot.kde()
plt.show()

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}


model = CmdStanModel(stan_file='bern_1.stan')
sample = model.sample(stan_data)
theta = sample.stan_variable('theta')
summary = sample.summary()


q5=numpy.quantile(theta,0.05)
q50=numpy.quantile(theta,0.5)
q95=numpy.quantile(theta,0.95)
qMean=theta.mean()

plt.figure()
plt.hist(theta, bins=50)
plt.axvline(q5, color='g')
plt.axvline(q50, color='r')
plt.axvline(q95, color='b')
plt.axvline(qMean, color='k')
plt.grid(True)
plt.legend(['5%','50%','95%','mean'])
plt.show()
