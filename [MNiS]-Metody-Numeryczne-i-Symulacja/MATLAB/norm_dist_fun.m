function [fx] = norm_dist_fun(x, mu, sigma)
    fx = 1./(sigma*sqrt(2*pi))*exp(-(x-mu).^2/(2*sigma^2));
end

