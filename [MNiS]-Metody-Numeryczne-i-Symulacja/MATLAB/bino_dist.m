function y = bino_dist(n, x, p)
   y = factorial(n)./(factorial(x).*factorial(n-x)) .* (p.^x) .* (1-p).^(n-x);
end

