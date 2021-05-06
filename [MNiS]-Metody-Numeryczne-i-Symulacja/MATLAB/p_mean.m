function x = p_mean(data,r)
    x = ( 1/length(data) * sum(data.^r) )^(1/r);
end

