function x = integral_simp(func,a,b,n)
    figure;
    hold on;
    
    if(mod(n,2)~=0)
        n=n+1;
    end
    
    h=(b-a)/n;
    x0=a;
    
    args=a:h:b;
    
    sum=0;
    
    for i=1:1:n/2
        f1 = func(args(2*i - 1));
        f2 = 4*func(args( 2*i ));
        f3 = func(args(2*i + 1));
        sum=sum+f1+f2+f3;
        area([args(2*i - 1) args(2*i) args(2*i + 1)], [f1 f2/4 f3]);
    end
    
    fplot(func, [a b]);
    x = 1/3 * h * sum;
end