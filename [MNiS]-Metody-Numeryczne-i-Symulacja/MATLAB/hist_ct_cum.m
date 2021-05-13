function x = hist_ct_cum(arr)
    n = length(arr);
    k = floor(sqrt(length(arr)));
    [counts, edges] = histcounts(arr, k,"Normalization","cumcount");
    figure;
    h = histogram("BinEdges", edges, "BinCounts", counts);
    
    hold on;
    mid_points = edges;
    plot(mid_points, [0 counts],'rx-');
    boxplot(arr, "orientation", "horizontal");
    plot(edges, 0.25*n*edges.^0, "color", "k");
    plot(edges, 0.5 *n*edges.^0, "color", "m");
    plot(edges, 0.75*n*edges.^0, "color", "b");
end

