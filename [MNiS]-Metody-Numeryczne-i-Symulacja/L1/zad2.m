#convert to decimal and use function from ex1.
clear all;
close all;

#INPUT

ipt_nb = "1100101";
ipt_sys = 2;

ipt_int = ipt_nb;
ipt_dec = "";

if (strfind(ipt_nb, ",")) #check if is floating point
  ipt_int = substr(ipt_nb, 1, strfind(ipt_nb, ",")-1);
  ipt_dec = substr(ipt_nb, strfind(ipt_nb, ",")+1);
end;
  
#INT

int_nb = 0;

for(i=0:(length(ipt_int)-1))
  temp1 = str2num(substr(ipt_int, length(ipt_int)-i, 1));
  int_nb = int_nb + temp1*ipt_sys^i;
end;

#DEC

dec_nb = 0;
for(i=1:length(ipt_dec))
  temp2 = str2num(substr(ipt_dec, i, 1));
  dec_nb = dec_nb + temp2*ipt_sys^(-i);
end;

opt_nb = int_nb + dec_nb;

#now convert decimal to desired system using script from ex2.