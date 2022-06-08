// data {
//    int N;
//    real Miles[N];
// }

// generated quantities {
//    real alpha = normal_rng(40000,8000);
//    real beta = lognormal_rng(0,1);
//    real sigma = exponential_rng(0.01);
//    real death[N];
//    for (i in 1:N) {
//        death[i] = normal_rng(Miles[i]*beta+alpha, sigma);
//    }
// }
data {
    int N;
    real deaths[N];
}

parameters {
   real mu;
   real<lower=0> sigma;
}

model {
   mu ~ normal(40000,8000);
   sigma ~ exponential(0.03);
   deaths ~ normal(mu,sigma);
}

generated quantities {
   real death = normal_rng(mu,sigma);
}