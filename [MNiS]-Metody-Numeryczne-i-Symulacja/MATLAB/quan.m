function x = quan(data, p)
    n=length(data);
    fpn = floor(p*n);
    
    if mod(p*n,2)==0
        x = data(fpn+1);
    else
        x = ( data(fpn) + data(fpn+1) )/2;
    end
end

