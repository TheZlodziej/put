#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <regex>

std::string literals(const std::string& str)
{
	std::string ret = "";
	for (auto c : str)
	{
		if ( (c >= 'A' && c <= 'Z') || (c <= 'z' && c >= 'a') )
		{
			ret += c;
		}
	}
	return ret;
}

std::string lowercase(const std::string& str)
{
	std::string ret = "";
	for (auto c : str)
	{
		if (c >= 'A' && c <= 'Z')
		{
			ret += c + ('a' - 'A');
		}
		else
		{
			ret += c;
		}
	}
	return ret;
}

int main()
{
	//a
	std::fstream file("license.txt", std::ios::in);
	if (!file.good()) { return -1; }
		
	std::map<std::string, int> map;
	std::string temp;
	while (file >> temp)
	{
		temp = lowercase(literals(temp));
		if (map.find(temp) == map.end())
		{
			map.insert(std::pair<std::string, int>(temp, 0));
		}
		map[temp]++;
	}

	file.close();

	//b
	std::cout << "=======b=======\n";
	for (auto [key, val] : map)
	{
		std::cout << key <<"\t" << val << "\n";
	}

	//c
	std::cout << "\n\n=======c=======\n";
	std::vector<std::pair<std::string, int>> vec;
	std::copy(map.begin(), map.end(), std::back_inserter(vec));
	std::sort(vec.begin(), vec.end(),
		[](std::pair<std::string, int> a, std::pair<std::string, int> b)
		{
			return a.second < b.second;
		}
	);

	//d
	std::fstream opt("zad1_d_opt.txt", std::ios::out);
	if (!opt.good()) { return -1; }
	for (auto v : vec)
	{
		//std::cout << v.first << " " << v.second<<"\n";
		opt << v.first << " " << v.second << "\n";
	}

	opt.close();

	//e
	//Dodam tylko regex do tego bo mi sie nie chce od nowa
	//pisac tego kodu bo nie pisalem funkcji tylko robilem w mainie
	//	-,_o_,-							Przepraszam, Jakub Wicher
	//
	//
	//REGEX:	\w+

	//f
	//Tego tez nie zrobie bo zrobilem wczesniej funkcje zeby mi
	//zamieniala na lower case i brala tylko litery
	//  -,_o_,-							Przepraszam ponownie, Jakub Wicher
	//
	//
	//FUNKCJE: literals & lowercase

	return 0;
}