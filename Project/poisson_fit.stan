data {
int M; //number of years analyzed
vector[M] miles; //number of miles driven
int y[M]; //number of fatal accidents
}
parameters {
real<lower=0>theta;
}
model {
theta ~ normal(0,0.1);
for (k in 1:M) {
y[k] ~ poisson(miles[k]*theta);
}
}
generated quantities {
   real y_sim[M];
  for (k in 1:M) {
    y_sim[k] = poisson_rng(miles[k]*theta);
  }
}