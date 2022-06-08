data {
    int N;
    vector[N] Miles;
    real deaths[N];
}

parameters {
    real alpha;
    real beta;
    real<lower=0> sigma;
}

transformed parameters {
   vector[N] mu = Miles*beta+alpha;
}

model {
   alpha ~ normal(40000,8000);
   beta ~ lognormal(0,1);
   sigma ~ exponential(0.08);
   deaths ~ normal(mu,sigma);
}

generated quantities {
    vector[N] log_lik;
   array [N] real death;
    for (i in 1:N) {
        log_lik[i] = normal_lpdf(deaths[i] | mu[i], sigma);
        death[i] = normal_rng(mu[i], sigma);
    }
}   