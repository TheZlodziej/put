function x = h_mean(data)
    if(any(data))
        s = sum(1./data);
        if(s ~= 0)
            x = length(data)/s;
        else
            disp("nie mozna wyliczyc sredniej harmonicznej");
            x = [];
        end
    else
        disp("nie mozna wyliczyc sredniej harmonicznej");
        x = [];
    end
end

