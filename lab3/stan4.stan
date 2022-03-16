data{
    int<lower=1> N;
}

generated quantities {
    realu mu = normal_rng(0, 1);
    real<lower=0> sigma = abs(normal_rng(0, 1));
    
    arrat[N] real y_prior;

    for(n in 1:N){
        y_prior = normal_rng(mu, sigma);
    }
    
}