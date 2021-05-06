function [x] = most_common(A)
    mc = A(1);
    mc_occ = 0;
    for i=1:length(A)
        curr_val = A(i);
        occ = 0;
        for j=1:length(A)
            if A(j) == curr_val
                occ = occ+1;
            end
        end
        
        if occ == mc_occ && ~any(mc(:)==curr_val)
            mc = [mc curr_val];
        end
        
        if occ>mc_occ
            mc_occ = occ;
            mc = curr_val;
        end
    end
    
    x=mc;
end

