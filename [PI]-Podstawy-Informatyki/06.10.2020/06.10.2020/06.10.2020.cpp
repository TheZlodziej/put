#include <iostream>

int main()
{
	std::cout << "Witaj, podaj jakas liczbe!\n";
	int target, guess, tries=0;
	std::cin >> target;
	std::cout << "Teraz zgadnij jaka liczbe mam w pamieci\n";	
	
	do
	{
		std::cin >> guess;

		if (guess < target)
			std::cout << "twoja liczba jest za mala.\n";

		if (guess > target)
			std::cout << "twoja liczba jest za duza.\n";

		tries++;
	} while (target != guess);

	std::cout << "\n\nbrawo udalo ci sie zgadnac liczbe - potrzebowales na to " << tries << " prob.";
}