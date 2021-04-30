#include <iostream>
#include <stdio.h>
#include <fstream>
#include "klasa.hpp"

void NazwaKlasy::Zapis()
{
    fstream plik;
    plik.open("osoby.txt", ios::out | ios::app);
    plik<< "Nazywam sie " << imie << " " << nazwisko << ", nr tel.:" << nr_telefonu << ", wiek:" << wiek << ", wzrost:" << wzrost << ", plec:" << plec << endl << endl;
    plik.close();
}

void NazwaKlasy::MetodaDane()
   {
    cout << endl << "Podaj imie: ";
    cin >> imie;
    getchar();

    cout << endl << "Podaj nazwisko: ";
    cin >> nazwisko;
    getchar();

    cout << endl << "Podaj nr telefonu: ";
    cin >> nr_telefonu;
    getchar();

    cout << endl << "Podaj wiek: ";
    cin >> wiek;
    getchar();

    cout << endl << "Podaj wzorst: ";
    cin >> wzrost;
    getchar();

    cout << endl << "Podaj plec: ";
    cin >> plec;
    getchar();
   };

void NazwaKlasy::MetodaPrzedstaw()
 {
  cout << endl;
  cout << "Witaj" << endl;
  cout << "Nazywam sie " << imie << " " << nazwisko << ", nr tel.:" << nr_telefonu << ", wiek:" << wiek << ", wzrost:" << wzrost << ", plec:" << plec << endl << endl;
 };