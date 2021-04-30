#include <iostream>
#include <vector>

struct osoba {
	std::string imie;
	std::string nazwisko;
};

osoba znajdz(std::vector<osoba> osoby, std::string imie)
{
	for (auto os : osoby)
	{
		if (os.imie == imie)
			return os;
	}
	return { {"brak"}, {"brak"} };
}

int main()
{
	std::vector<osoba> osoby{ {"jakub", "wicher"}, {"norbert", "gierczak"} };
	std::cout<<znajdz(osoby, "jakub").nazwisko;
	return EXIT_SUCCESS;
}