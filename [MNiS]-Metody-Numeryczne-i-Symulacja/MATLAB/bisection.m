function [mz] = bisection(func, min, max, delta)  
    if ~exist("delta", "var")
        delta = 0.0001;
    end
    % wykres    
    figure;
    hold on;
    fplot(func, [min max]);
    fplot(@(x) zeros(size(x)), [min max]);
    
    % mz
    mz=[];
    
    a=min;
    b=max;
    
    fa = func(a);
    fb = func(b);
    iter=0;
    
    if(fa*fb<0)
        while(1)
            iter=iter+1;
            x1=(a+b)/2;
            fx1=func(x1);
            plot(x1,0, ".", "MarkerSize", 8+iter);
            
            if(abs(fx1)<=delta)
                mz = [x1];
               break;
            end
            
            if(fa*fx1<0)
               b = x1;
               fb = func(b);
            elseif(fx1*fb<0)
               a = x1;
               fa = func(a);
            end        
        end
    elseif(fa*fb==0)
        if(fa==0)
            mz=[fa];
        else
            mz=[fb];
        end
    else
        disp(strcat("f nie ma miejsc zerowych w przedziale [",num2str(min),"; ",num2str(max),"]"));
    end
end