clc; clear all; close all;

% x' = Ax + Bu
% u = u_ref - Kx
% x' = Ax + B(u_ref - Kx)
% x' = (A - BK)x + Bu_ref 
% H = (A - BK)
% x' = Hx + Bu_ref

% new system is stable if real part of
% all eigenvalues is negative
% (are on the LHS of imaginary lambda plane)
% |lambda*I-A2| = 0 => { lambda1, lambda2, ... }

% to apply full state feedback, 
% base system has to be controlable

A = [0 1; -4 -1];
B = [0; 2];
C = [1 0];
D = 0;

