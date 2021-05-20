function [fx] = exp_dist_fun(x, mu)
    fx = 1/mu * exp(-1/mu * x);
end

