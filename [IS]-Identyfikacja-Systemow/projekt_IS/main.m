clc;
close all;
clear all;
load("HILSys.mat");

% wariant 03
%   identyfikacja metodą LS
%   model dynamiczny czasu dyskretnego
%   identyfikacja typu BLACK-BOX

s = tf('s');

% ustawienia symulacji
Tp = 0.01; % s

t = 0.006:0.01:29.995+0.01; % sam wygenerowałem bo potrzebuję stałe Tp.

%% próba ręcznego dopasowania do obiektu
k = 1;
wn = 2.78;
ksi = 0.33;
Gs = k*wn^2/(s^2 + 2*ksi*wn*s + wn^2);
Gz = c2d(Gs, Tp);

% RDP - ręcznie dobierane parametry
y_RDP = lsim(Gz, u, t);

%% transimtancja dyskretna z parametrami -> dyskretyzacja ZOH
%
%          (b0 + b1 * z^-1) * z^-1
% G(z) = ---------------------------
%         1 + a1 * z^-1 + a2 * z^-2
%
% ARMA
% y(t) = -a1*y(t-1) -a2*y(t-2) +b0*u(t-1) +b1*u(t-2)
% Theta = [a1 a2 b0 b1]'

%% przygotowanie wektorów do estymacji | model ARMA
param_vec_len = 4;
max_delay = 2;
N = length(t) - max_delay;

% obliczenia symulacyjne (znamy cały przebieg)
phi = [
        -y(2:end-1), ...
        -y(1:end-2), ...
        +u(2:end-1), ...
        +u(1:end-2)
    ];

% obliczenia iteracyjne
% phi = zeros(N, param_vec_len);
% for i = 1:N
%    phi(i, :) = [
%        -y(max_delay + i - 1), ...
%        -y(max_delay + i - 2), ...
%        +u(max_delay + 1 - 1), ...
%        +u(max_delay + i - 2);
%    ];
% end

theta = pinv(phi) * y(max_delay + 1 : end);

%% Wykreslenie odpowiedzi obiektu na wymuszenie, po identyfikacji LS
% a0 = 1;
a1 = theta(1);
a2 = theta(2);
b0 = theta(3);
b1 = theta(4);

% rozwiązanie symulacyjne (znamy cały przebieg)
y_IDENT = [
    0;
    0;
    ( ...
        -a1 * y(2 : end - 1) ...
        -a2 * y(1 : end - 2) ...
        +b0 * u(2 : end - 1) ...
        +b1 * u(1 : end - 2) ...
    )
];

% rozwiązanie iteracyjne
% y_IDENT = zeros(size(y));
% for i = 1:N
%     % y(t) = -a1*y(t-1) -a2*y(t-2) +b0*u(t-1) +b1*u(t-2)
%     y_IDENT(max_delay + i) = ...
%        -a1 * y(max_delay + i - 1) ...
%        -a2 * y(max_delay + i - 2) ...
%        +b0 * u(max_delay + i - 1) ...
%        +b1 * u(max_delay + i - 2);
% end

%% Wskaźniki
n = length(y);
avg_error = sum(abs(y - y_IDENT))/n;
mean_squared_error = sqrt(sum((y - y_IDENT).^2)/n);

