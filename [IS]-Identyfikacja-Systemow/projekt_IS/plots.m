%% identyfikacja wstepna
figure;
hold on;
title('WE/WY (t) - Wstępna identyfikacja');
plot(t, y, 'b', t, u, 'r');
legend('y', 'u');
% na podstawie pomiarów, można stwierdzić, że odpowiedź obiektu ma
% charakter obiektu oscylacyjnego

%% ręcznie dobrane parametry
figure;
hold on;
title('Ręcznie dobrane parametry - Wstępna identyfikacja');
plot(t, y, 'b', t, y_RDP, 'r', t, u, '-g');
legend('y', 'y ręcznie dobrane', 'u');

%% estymacja LS
figure;
hold on;
title('Estymacja LS');
plot(t, y, 'b', t, y_IDENT, 'r', t, u, '-g');
legend('y', 'y estymowane', 'u');