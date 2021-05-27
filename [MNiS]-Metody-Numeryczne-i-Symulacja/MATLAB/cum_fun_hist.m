function x = cum_fun_hist(data, k)
    figure;
    hold on;
    
    if ~exist('k','var')
        k = floor(sqrt(length(data)));
    end
    
    [counts, edges] = histcounts(data, k, 'Normalization', 'cdf');
    x = histogram("BinEdges", edges, "BinCounts", counts);
end

