from cmdstanpy import CmdStanModel
import pandas as pd
import arviz as az 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

model = CmdStanModel(stan_file='stan1.stan')

result = model.sample(data={'N':1, 'y':[1]}, 
                            seed = 9012022,
                            chains = 4)

print(result.diagnose)

#Convertion to arviz InferenceData
arviz_result = az.from_cmdstanpy(
    posterior=result
)
#Calculating log sigma
post = arviz_result.posterior
post["log_sigma"] = np.log(post["sigma"])
arviz_result
#Arviz plot
az.plot_pair(arviz_result, var_names=['mu', 'log_sigma'], divergences=True)
plt.show()

model = CmdStanModel(stan_file='stan1.stan')
result = model.sample(data={'N':5, 'y':[1.05, 0.87, -0.49, -0.22, 0.18]}, 
                            seed = 9012022,
                            chains = 4)
print(result.diagnose())

#Convertion to arviz InferenceData
arviz_result = az.from_cmdstanpy(
    posterior=result
)

#Calculating log sigma
post = arviz_result.posterior
post["log_sigma"] = np.log(post["sigma"])
arviz_result

#Arviz plot
az.plot_pair(arviz_result, var_names=['mu', 'log_sigma'], divergences=True)
plt.show()

#EX2

df = pd.read_csv("coin.csv")

y = df['Toss_Result']
N = len(y)

model = CmdStanModel(stan_file='stan2.stan')
result = model.sample(data={"N" : N, "y" : y}, 
                           seed = 9012022,
                           chains = 4)

result.summary()
#Convertion to arviz InferenceData
arviz_result = az.from_cmdstanpy(
    posterior=result
)
print(arviz_result)

#Plot
az.plot_density(arviz_result,shade=0.1)
plt.show()