close all;
clear all;

j=25;
rng(j);
n=100;

% A

mu=5;
sigma=3;
data_norm=normrnd(mu,sigma,1,n);

% B

data_mean = a_mean(data_norm);
data_var = var_sample(data_norm);
data_dev = stand_dev_sample(data_norm);

% C.1:

X=mu-3*sigma:0.1:mu+3*sigma;

fe1 = @(x) norm_dist_fun(x, mu, sigma);
fe2 = @(x) norm_dist_fun(x, data_mean, data_dev);

dens_fun_hist(data_norm);
plot(X, fe1(X));
plot(X, fe2(X));

% C.2:

FE1 = @(x) integral_trap(fe1, mu-3*sigma, x, 10);
FE2 = @(x) integral_trap(fe2, mu-3*sigma, x, 10);

emp_dist_hist(data_norm);
plot(X, FE1(X));
plot(X, FE2(X));

% exp dist
clear all;

n=100;
j=25;
rng(j);
mu_exp=2;

data_exp = exprnd(mu_exp,1,n);
exp_data_mean = a_mean(data_exp);
X = 0:0.01:10;

fc1 = @(x) exp_dist_fun(x, mu_exp);
fc2 = @(x) exp_dist_fun(x, exp_data_mean);

FC1 = @(x) integral_trap(fc1, 0, x, 10);
FC2 = @(x) integral_trap(fc2, 0, x, 10);

cum_fun_hist(data_exp);
plot(X, FC1(X));
plot(X, FC2(X));

dens_fun_hist(data_exp);
plot(X, fc1(X));
plot(X, fc2(X));

% poisson & binominal fun

clear all;

n=100;
j=25;
rng(j);

bino_N = 15;
bino_p = 0.75;

X=0:bino_N;

% bino
data_bino = binornd(bino_N, bino_p, 1, n);
bino_mean = a_mean(data_bino);
bino_var = var_sample(data_bino);

dens_fun_hist(data_bino);
plot(X, bino_dist(bino_N, X, bino_p), "xr"); % with given data
plot(X, bino_dist(bino_N, X, 1/bino_N*a_mean(data_bino)), "xg"); % estimated

% poiss

X=0:20;
poiss_lambda = 2;

data_poiss = poissrnd(poiss_lambda, 1, n);
poiss_mean = a_mean(data_poiss);
poiss_var = var_sample(data_poiss);

dens_fun_hist(data_poiss);
stairs(X, poiss_dist(poiss_lambda, X), "Color", "r");
stairs(X, poiss_dist(a_mean(data_poiss), X), "Color", "g");


