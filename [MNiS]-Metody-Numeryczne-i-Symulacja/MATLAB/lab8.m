clear all;
close all;
f = @(x) x.^3 - 5*x.^2 - 3*x - 7;

%integral_sq(f,6,10,10)
integral_trap(f,6,10,4)
%integral_simp(f,6,10,100)
%integral_mtcl(f,6,10,100)