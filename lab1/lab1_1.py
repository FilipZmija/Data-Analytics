import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

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
