function x = integral_sq(func, a, b, n)
    figure;
    hold on;
    
    h = (b-a)/n;
    x0=a;
    sum=0;
    
    for i=1:n
        mid=func((2*x0+h)/2);
        sum = sum + mid;
        area([x0, x0+h], [mid, mid]);
        x0=x0+h;
    end
    
    fplot(func, [a b],"LineWidth",4, "Color", "k");
    x=h*sum;
end