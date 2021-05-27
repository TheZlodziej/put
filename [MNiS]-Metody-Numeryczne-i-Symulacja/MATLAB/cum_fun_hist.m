function x = cum_fun_hist(data)
    figure;
    hold on;
    k = floor(sqrt(length(data)));
    
    [counts, edges] = histcounts(data, k, 'Normalization', 'cdf');
    x = histogram("BinEdges", edges, "BinCounts", counts);
end

