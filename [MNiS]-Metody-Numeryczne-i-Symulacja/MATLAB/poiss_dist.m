function y = poiss_dist(lambda,x)
    y = lambda.^x./factorial(x) .* exp(-1*lambda);
end

