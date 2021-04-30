close all;
clear all;

num = 1024; #number in decimal system
sys = 2; #system you want your number in

#INT PART

num_int_part = floor(num);

new_sys_int = "";

while(num_int_part > sys)
  temp1 = idivide(num_int_part,sys, "floor");
  new_sys_int = strcat(mat2str(num_int_part - sys*temp1), new_sys_int);
  num_int_part = temp1;
end;

new_sys_int = strcat(mat2str(num_int_part), new_sys_int);

#DEC PART

num_dec_part = num-floor(num); #take the decimal part

new_sys_dec = "";
precision = 0;

while( (num_dec_part != 0) && (precision!=10) )
  temp = num_dec_part * sys;
  new_sys_dec = strcat(new_sys_dec, mat2str(floor(temp)));
  num_dec_part = temp - floor(temp);
  precision = precision+1;
end;

#CONNECTING BOTH SECTIONS

new_sys = "";

if (strcmp(new_sys_dec,""))
  new_sys = new_sys_int;
else
  new_sys = strcat(new_sys_int, ",", new_sys_dec);
end;