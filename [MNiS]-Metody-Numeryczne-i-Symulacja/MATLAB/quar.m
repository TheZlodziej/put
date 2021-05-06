function x = quar(data)
    data = sort(data);
    
    Q1 = quan(data, 0.25);
    Q2 = quan(data, 0.5);
    Q3 = quan(data, 0.75);
    
    x = [Q1 Q2 Q3];
end

