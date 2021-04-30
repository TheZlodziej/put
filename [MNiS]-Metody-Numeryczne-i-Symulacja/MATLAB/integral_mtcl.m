function x = integral_mtcl(func,a,b,n)
    %sum=0;
    args=a+(b-a)*rand(1,n);
    vals=func(args);
    x=(b-a)/n * sum(vals);
end