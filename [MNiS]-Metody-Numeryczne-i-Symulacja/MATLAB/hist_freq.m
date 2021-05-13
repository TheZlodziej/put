function x = hist_freq(arr)
    k = floor(sqrt(length(arr)));
    [counts, edges] = histcounts(arr, k,"Normalization","probability");
    figure;
    h = histogram("BinEdges", edges, "BinCounts", counts);
    
    hold on;
    len = h.BinWidth;
    mid_points = [edges(1)-len/2 edges+len/2];
    plot(mid_points, [0 counts 0],'rx-');
end
