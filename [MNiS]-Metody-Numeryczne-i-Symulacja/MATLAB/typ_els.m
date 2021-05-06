function x = typ_els(data)
    m = a_mean(data);
    sd = stand_dev(data);
    x = [];
    for i=1:length(data)
       if data(i) < m+sd && data(i) > m-sd
            x = [x data(i)];
       end
    end
end