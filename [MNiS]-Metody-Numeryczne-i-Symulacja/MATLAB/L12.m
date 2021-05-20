close all;

j=25;
s=rng(j);
n=100;

% A

mu=5;
sigma=3;
data_norm=normrnd(mu,sigma,1,n);
data_exp=exprnd(mu,1,n);

% B

data_mean = a_mean(data_norm);
data_var = var_sample(data_norm);
data_dev = stand_dev_sample(data_norm);

% C.1:

X=mu-3*sigma:0.1:mu+3*sigma;

f1 = @(x) norm_dist_fun(x, mu, sigma);
f2 = @(x) norm_dist_fun(x, data_mean, data_dev);

dens_fun_hist(data_norm);
plot(X, f1(X));
plot(X, f2(X));

% C.2:

F1 = @(x) integral_trap(f1, mu-3*sigma, x, 10);
F2 = @(x) integral_trap(f2, mu-3*sigma, x, 10);

emp_dist_hist(data);
plot(X, F1(X));
plot(X, F2(X));

% nwm co to bylo cos tam z exponential distribution; chyba na nastepnej
% lekcji bedzie
data = exprnd(mu,1,n);

dens_fun_hist(data);
fplot(@(x) exp_dist_fun(x, mu));
fplot(@(x) exp_dist_fun(x, data_mean));




