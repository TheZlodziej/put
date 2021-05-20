function x = var_sample(data)
    n=length(data);
    x_m = a_mean(data);
    x=0;
    for i=1:n
        x = x + (data(i)-x_m)^2;
    end
    x = x*1/(n-1);
end

