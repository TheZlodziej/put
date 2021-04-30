function [mz] = bisection_ood(func, min, max, ood, delta)

    if ~exist("delta", "var")
        delta = 0.0001;
    end
    
    mz = [];
    
    for i=1:length(ood)
        mz=[mz bisection(func, min, ood(i)-delta, delta)];
        min=ood(i)+delta;
    end
        mz=[mz bisection(func, min, max, delta)];
end