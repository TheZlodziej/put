#include <iostream>
#include <ctime>

class Zwierzak {
protected:
	float _masa;
	float _wiek;
public:
	Zwierzak(float masa=0, float wiek=0)
	{
		std::cout << "konstruktor zwierzak\n";
		_masa = masa;
		_wiek = wiek;
	}

	void patrz()
	{
		return;
	}

	void oddychaj()
	{
		return;
	}

	virtual void zyj()
	{
		std::cout << "zyje i mam sie dobrze\n";
	}
};

/////////////////////////////

class Ryba : public Zwierzak {
public:
	Ryba()
	{
		std::cout << "konstruktor ryba\n";
	}

	void plyn() 
	{
		return;
	}

	void zyj()
	{
		std::cout << "zyje i plywa mi sie swietnie\n";
	}
};

class Ssak : public Zwierzak {
public:
	void biegnij()
	{
		return;
	}
};

class Ptak : public Zwierzak {
public:
	void lec()
	{
		return;
	}
};

/////////////////////////////

class Welonek : public Ryba {

};

class Nemo : public Ryba {
public:
	Nemo()
	{
		std::cout << "konstruktor nemo\n";
	}
};

class Karp : public Ryba {

};

//////////////////////////////

class Lew : public Ssak {

};

class Pies : public Ssak {

};

class Slon : public Ssak {

};

//////////////////////////////

class Papuga : public Ptak {

};

class Kanarek : public Ptak {

};

class Golab : public Ptak {

};

//////////////////////////////

int main()
{
	//Nemo nemo; //narpiew konstruktor ojca wszechwiedzacego potem dzieci po kolei od gory do dolu
	//nemo.zyj();
	Zwierzak* zwierze = nullptr;
	srand(time(0));
	unsigned int los = std::rand() % 3;
	switch (los)
	{
	case 0:
		zwierze = new Nemo();
		break;

	case 1:
		zwierze = new Papuga();
		break;

	case 2:
		zwierze = new Pies();
		break;
	}

	zwierze->zyj();

	return 0;
}