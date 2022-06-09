generated quantities {
   real mu = normal_rng(33000,5000);
   real sigma = exponential_rng(0.001);
   real deaths = normal_rng(mu,sigma);
}
// around 10 ppl a day in Poland -> 3650 in poland per 38mln ppl, so in USA 9x more ppl in usa so around 33000 ppl yearly in USA nowadays