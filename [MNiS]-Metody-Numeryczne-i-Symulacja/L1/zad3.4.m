clear all;
close all;

#load data
sin_vals = load("sine.txt");
sin_noise = load("sine_with_noise.txt");
sin_args = load("arguments_of_sine.txt");

#3:
  #a
  abs_err_sin = abs(sin_vals.-sin_noise);
  figure;
  hold on;
  plot(sin_args, abs_err_sin, "-");
  plot(sin_args, sin_vals, "-", "linewidth", 2);
  title("Blad bezwzgledny");
  xlim([0, 360]);
  ylim auto;
  xlabel('x');
  ylabel('f(x)');
  legend("Blad bezwzgledny", "f(x) = sin(x)", "Location", "southwest");
  
  #b
  rel_err_sin = [];
  for(i=1:rows(abs_err_sin))
    if (abs(sin_vals(i)) < 0.0001)
      rel_err_sin(end+1,:) = 0;
    else
      rel_err_sin(end+1,:) = abs_err_sin(i)/sin_vals(i);
    end;
  end;
  
  figure;
  hold on;
  plot(sin_args, rel_err_sin, "-");
  plot(sin_args, sin_vals, "-", "linewidth", 2);
  title("Blad wzgledny");
  xlim([0,360]);
  ylim([min(rel_err_sin),max(rel_err_sin)]);
  xlabel('x');
  ylabel('sin(x)');
  legend("Blad wzgledny", "f(x) = sin(x)", "Location", "northeast");
 
  #c
  avg_abs_err = sum(abs_err_sin)/rows(abs_err_sin);

  #d
  avg_rel_err = sum(rel_err_sin)/rows(rel_err_sin);

  #e
  eff_sin = max(sin_vals)/sqrt(2);
  eff_noise = max(sin_noise)/sqrt(2);
  
#4:
  corrected_sin_vals = [];
  for (i=1:rows(sin_noise))
    if (sin_noise(i) >= sin_vals(i))  
      corrected_sin_vals(end+1,:) = sin_noise(i) - avg_abs_err;
    else
      corrected_sin_vals(end+1,:) = sin_noise(i) + avg_abs_err;
    end;
  end;
  
  figure;
  hold on;
  plot(sin_args, corrected_sin_vals, "-");
  plot(sin_args, sin_vals, "-", "linewidth", 2);
  title("Poprawione wartosci sinusa");
  xlim([0, 360]);
  ylim auto;
  xlabel('x');
  ylabel('f(x)');
  legend("Poprawione wartosci sinus", "f(x) = sin(x)", "Location", "northeast");
  
  psd = sqrt(sum(corrected_sin_vals)^2 / rows(corrected_sin_vals));
  
  #b
  avg_sq_err_noise = sqrt( (sin_noise - mean(sin_noise)).^2 / (rows(sin_noise)*(rows(sin_noise)-1) ));
  avg_sq_err_corrected = sqrt( (corrected_sin_vals - mean(corrected_sin_vals)).^2 / (rows(corrected_sin_vals)*(rows(corrected_sin_vals)-1) ));
  