function x = integral_trap(func,a,b,n)
    %figure;
    %hold on;
    h=(b-a)/n;
    x0=a;
    sum=0;
    
    for i=1:n
        sum=sum+func(x0)+func(x0+h);
        %area([x0, x0+h], [func(x0), func(x0+h)]);
        x0=x0+h;
    end
    
    %fplot(func, [a b], "LineWidth", 4, "Color", "k");
    x=h/2 .* sum;
end