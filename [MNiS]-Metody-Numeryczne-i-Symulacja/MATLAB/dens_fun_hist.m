function x = dens_fun_hist(data)
    figure;
    hold on;
    k = floor(sqrt(length(data)));
    
    [counts, edges] = histcounts(data, k, 'Normalization', 'pdf');
    x = histogram("BinEdges", edges, "BinCounts", counts);
end

