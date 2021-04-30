#include <stdio.h>
#include <iostream>
#include "klasa.hpp"

void search(NazwaKlasy tab[3], string arg_nr_tel)
{
	for (int i = 0; i < 3; i++)
	{
		if (tab[i].nr_telefonu == arg_nr_tel)
		{
			tab[i].MetodaPrzedstaw();
			tab[i].Zapis();
			return;
		}
	}
}

int main(int argc, char* argv[])
{
	NazwaKlasy osoby[3];
	for(int i=0; i<3; i++)
	{
		osoby[i].MetodaDane();
	}

	for (int i = 0; i < 3; i++)
	{
		osoby[i].MetodaPrzedstaw();
	}

	search(osoby, "123");

	getchar();
	return 0;
};


