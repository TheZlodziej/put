close all;
clear all;

#z1

A=[-11 -2 5 6 -9; -3 7 0 -5 4; 7 0 2 4 -3; 2 5 0 -13 4; -6 5 -4 7 0];
b=[32; 8; 43; -20; 40];

#Ax=b => inv(A)*A*x=int(A)*b => Ix=inv(A)*b => x = inv(A)*b
x = inv(A)*b;

#z2 && z3
a=1;
b=-2;
c=3;
x=[];
if (a!=0)
  delta = b^2 - 4*a*c;
  if (delta == 0)
    x=[-b./(2.*a)];
  #elseif (delta<0)
  #  x=[(-b-i*sqrt(-delta))/(2*a), (-b+i*sqrt(-delta)/(2*a))];
  else
    x=[ -b/(2*a)-sqrt(delta)/(2*a), -b/(2*a)+sqrt(delta)/(2*a)];
  endif;
  
  #z2 chart
  #preparing data
  args=[-5:0.1:5];
  vals=[];
  for (i=-5:0.1:5)
    vals(end+1, :) = a*i*i+b*i+c;
  endfor;
  
  #displaying chart
  figure;
  hold on;
  plot(args,vals,'r-');
  #make the chart pretty uwu
  title("f(x)=ax^2 + bx + c");
  xlim([-5,5]);
  ylim ([min(vals), max(vals)]);
  xlabel("x");
  ylabel("f(x)");
  #x,y axis
  xL = xlim;
  yL = ylim;
  line([0 0], yL, "color", "k", "linestyle", "-");
  line(xL, [0 0], "color", "k", "linestyle", "-"); 
  legend(strcat("f(x)=", num2str(a), "x^2 + (", num2str(b), ")x + ", num2str(c) ), "os x", "os y");
else
  disp("to nie jest rownanie kwadratowe");
  
endif;
