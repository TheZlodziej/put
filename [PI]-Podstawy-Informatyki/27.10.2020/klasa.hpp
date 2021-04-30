#ifndef KLASA_HPP_INCLUDED
#define KLASA_HPP_INCLUDED

using namespace std;

class NazwaKlasy
{
private:
    string imie;
    string nazwisko;
    int wiek;
    float wzrost;
public:
    string nr_telefonu;
    char plec;
    void MetodaDane();
    void MetodaPrzedstaw();
    void Zapis();
};

#endif // KLASA_HPP_INCLUDED
