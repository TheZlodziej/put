%% identyfikacja wstepna
figure;
hold on;
title('WE/WY (t) - Wstępna identyfikacja');
plot(t, y, 'b', t, u, 'r');
legend('y', 'u');
xlabel('t [s]');
ylabel('y(t) / u(t)');
grid on;
% na podstawie pomiarów, można stwierdzić, że odpowiedź obiektu ma
% charakter obiektu oscylacyjnego

%% ręcznie dobrane parametry
figure;
hold on;
title('Ręcznie dobrane parametry - Wstępna identyfikacja');
plot(t, y, 'b', t, y_RDP, 'r', t, u, '-g');
legend('y', 'y ręcznie dobrane', 'u');
xlabel('t [s]');
ylabel('y(t) / u(t)');
grid on;

%% estymacja LS
figure;
hold on;
title('Estymacja LS');
plot(t, y, 'b', t_valid, y_est, 'r', t, u, '-g');
xlim([t_valid(1), t_valid(end)])
legend('y', 'y estymowane', 'u');
xlabel('t [s]');
ylabel('y(t) / u(t)');
grid on;

%% Odpowiedź na inny sygnał (sin)
figure;
hold on;
title('Odpowiedź estymowanego obiektu na u = sin(2*pi*t)');
plot(t_iw, u_iw, 'b', t_iw, y_iw, 'r');
legend('u = sin(t)', 'y estymowane');
xlabel('t [s]');
ylabel('u(t) / y(t)');
grid on;

%% Analiza stabilności (rlocus)
figure;
rlocus(Ob);