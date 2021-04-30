clear all;
close all;
x=[-2*pi:0.1:2*pi];
y=sin(x);
figure
plot(x,y,'b','linewidth',2)

hold on
plot(x, x.^0-1,'k')

plot(x.^0-1,x,'k')


xlabel('x')
ylabel('f(x)')
xlim([-2*pi 2*pi]);
ylim([-2*pi 2*pi]);
title('$f(x)= \sin(x)$','Interpreter','latex','FontSize', 14)

leg1 = legend('$f(x)=\sin(x)$','os x','os y','Location','best');
set(leg1,'Interpreter','latex');