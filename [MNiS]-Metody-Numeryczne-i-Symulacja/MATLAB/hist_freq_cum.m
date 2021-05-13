function x = hist_freq_cum(arr)
    n = length(arr);
    k = floor(sqrt(length(arr)));
    [counts, edges] = histcounts(arr, k,"Normalization","cdf");
    figure;
    h = histogram("BinEdges", edges, "BinCounts", counts);
    
    hold on;
    mid_points = edges;
    plot(mid_points, [0 counts],'rx-');
end
