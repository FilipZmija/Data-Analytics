data {
    int N;
    real deaths[N];
}

parameters {
   real mu;
   real<lower=0> sigma;
}

model {
   mu ~ normal(33000,5000);
   sigma ~ exponential(0.001);
   deaths ~ normal(mu,sigma);
}

generated quantities {
   real death = normal_rng(mu,sigma);
}