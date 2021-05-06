function x = pos_coeff_var(A)
    quars = quar(A);
    x = quar_dev(A)/quars(2);
end

