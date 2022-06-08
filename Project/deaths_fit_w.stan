data {
    int N;
    vector[N] Miles;
    real deaths[N];
}

parameters {
    real alpha;
    real beta;
    real theta;
    real<lower=0> sigma;
}

transformed parameters {
   vector[N] mu = beta*(Miles^2)+Miles*alpha+theta;
}

model {
   alpha ~ normal(0, 1);
   beta ~ normal(0, 1);
   theta ~ normal(40000,8000);
   sigma ~ exponential(0.1);
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