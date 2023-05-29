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
t = (0.006:0.01:29.995+0.01)'; % sam wygenerowałem bo potrzebuję stałe Tp.

% przygotowanie danych do identyfikacji / validacji
procent_valid = 0.3;
length_valid = floor(0.3 * length(t));

y_ident = y(1 : length(t) - length_valid);
u_ident = u(1 : length(t) - length_valid);
t_ident = t(1 : length(t) - length_valid);

y_valid = y(length(t) - length_valid + 1 : end);
u_valid = u(length(t) - length_valid + 1 : end);
t_valid = t(length(t) - length_valid + 1 : end);

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
% obliczenia symulacyjne (znamy cały przebieg)
max_delay = 2;

phi = [
        -y_ident(2:end-1), ...
        -y_ident(1:end-2), ...
        +u_ident(2:end-1), ...
        +u_ident(1:end-2)
    ];

% obliczenia iteracyjne
% N = length(t_ident) - max_delay;
% param_vec_len = 4;
% phi = zeros(N, param_vec_len);
% for i = 1:N
%    phi(i, :) = [
%        -y_ident(max_delay + i - 1), ...
%        -y_ident(max_delay + i - 2), ...
%        +u_ident(max_delay + 1 - 1), ...
%        +u_ident(max_delay + i - 2);
%    ];
% end

theta = pinv(phi) * y_ident(max_delay + 1 : end);

%% Wykreslenie odpowiedzi obiektu na wymuszenie, po identyfikacji LS
% a0 = 1;
a1 = theta(1);
a2 = theta(2);
b0 = theta(3);
b1 = theta(4);

% rozwiązanie symulacyjne (znamy cały przebieg)
y_est = [
    y_valid(1);
    y_valid(2);
    ( ...
        -a1 * y_valid(2 : end - 1) ...
        -a2 * y_valid(1 : end - 2) ...
        +b0 * u_valid(2 : end - 1) ...
        +b1 * u_valid(1 : end - 2) ...
    )
];

% rozwiązanie iteracyjne
% y_est = zeros(size(y));
% for i = 1:N
%     % y(t) = -a1*y(t-1) -a2*y(t-2) +b0*u(t-1) +b1*u(t-2)
%     y_est(max_delay + i) = ...
%        -a1 * y_valid(max_delay + i - 1) ...
%        -a2 * y_valid(max_delay + i - 2) ...
%        +b0 * u_valid(max_delay + i - 1) ...
%        +b1 * u_valid(max_delay + i - 2);
% end

%% Wskaźniki
n = length(y_valid);
avg_error = sum(abs(y_valid - y_est))/n;
mean_squared_error = sum((y_valid - y_est).^2)/n;
J_fit = (1 - norm(y_valid - y_est)/norm(y_valid - mean(y_valid)*ones(size(y_valid)))) * 100; % [%]

%% Odpowiedź układu na inne wymuszenie
Ob = tf([b0, b1, 0], [1, a1, a2], Tp);
t_iw = 0:Tp:10;
u_iw = sin(2*pi*t_iw);
y_iw = lsim(Ob, u_iw, t_iw);
