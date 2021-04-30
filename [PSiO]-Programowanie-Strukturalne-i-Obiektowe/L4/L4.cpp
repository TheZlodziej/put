/////////////////////////////zadanie pdosumowujace
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


/////////////////////////////zadanie domowe
/*
#include <iostream>
#include <regex>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

std::string get_data(const std::string& fn)
{
    std::fstream f(fn, std::ios::in);
    if (!f.good()) { return ""; }

    std::string ret("");
    
    std::stringstream ss;
    ss << f.rdbuf();
    ret = ss.str();

    f.close();
    return ret;
}

std::vector<std::string> zad1_a(std::string data)
{
    std::vector<std::string> ret;
    std::regex re(R"(<a\s+(?:[^>]*?\s+)?href=(["'])(.*?)\1)");
    std::smatch m;
    while (std::regex_search(data, m, re))
    {
        ret.push_back(m[2]);
        data = m.suffix();
    }
    return ret;
}

std::vector<std::string> zad1_b(std::string data)
{
    std::vector<std::string> ret;
    std::regex re(R"(\s{1,}(\+\d{1,3}|\(\d{1,3}\)|0{1,})?\s?\d{1}((\s|\-)?\d{1}){8})");
    std::smatch m;
    while (std::regex_search(data, m, re))
    {
        ret.push_back(m[0]);
        data = m.suffix();
    }
    return ret;
}

std::map<std::string, std::vector<std::string>> zad1_c(std::string data)
{
    std::map<std::string, std::vector<std::string>> ret;
    std::regex re(R"(<div class="g">)");
    std::smatch m;
    while (std::regex_search(data, m, re))
    {
        std::string curr_div = data.substr(0, data.find(m[0]));
        std::string href = zad1_a(curr_div)[0];
        std::vector<std::string> phone_nbs = zad1_b(curr_div);
        if (ret.find(href) == ret.end())
        {
            ret.insert(std::pair<std::string, std::vector<std::string>>(href, phone_nbs));
        }
        else
        {
            ret.at(href).insert(ret.at(href).end(), phone_nbs.begin(), phone_nbs.end());
        }
        data = m.suffix();
    }
    return ret;
}

std::vector<std::string> zad1_d(const std::vector<std::string>& data, const std::string& chars = " -()+")
{
    std::vector<std::string> ret;
    for (const auto& str : data)
    {
        std::string t = "";
        for (const auto& c : str)
        {
            if (chars.find(c) == std::string::npos)
            {
                t += c;
            }
        }
        ret.push_back(t);
    }
    return ret;
}

std::string zad1_e_1(std::string data)
{
    std::regex re(R"(http(s)?:\/\/(.+?(?=\/)))");
    std::smatch m;
    if (std::regex_search(data, m, re))
    {
        return m[m.size()-1];
    }
    return data;
}

std::map<std::string, std::vector<std::string>> zad1_e_2(const std::map<std::string, std::vector<std::string>>& data)
{
    std::map<std::string, std::vector<std::string>> ret;
    for (auto [href, nbs] : data)
    {
        std::string domain = zad1_e_1(href);
        if (ret.find(domain) == ret.end())
        {
            ret.insert(std::pair<std::string, std::vector<std::string>>(domain, nbs));
        }
        else
        {
            ret.at(domain).insert(ret.at(domain).end(), nbs.begin(), nbs.end());
        }
    }
    return ret;
}

void zad1_f()
{
    std::cout << "zad 1 f) zrobilem bo sprawdzalem czy moja mapa ma juz dany klucz i jak ma to dolaczalem do wartosci dla danego klucza numery telefonow xd";
}

void zad1_g(const std::map<std::string, std::vector<std::string>>& data)
{
    std::fstream opt("zad1_g_opt.csv", std::ios::out);
    if (!opt.good()) { return; }

    opt << "Link,Nr tel\n";

    for (auto [href, nbs] : data)
    {
        opt << href << ",";

        for (auto nb : nbs)
        {
            opt << nb << ",";
        }

        opt << "\n";
    }

    opt.close();
}

int main()
{
    std::string data = get_data("plik3.html");

    std::vector<std::string> x = zad1_b(data);

    /*x = zad1_d(x);
    for (auto c : x)
    {
        std::cout << c << "\n";
    }

    x = zad1_a(data);
    for (auto c : x)
    {
        std::cout << c << "\n";
    }*/

    std::map<std::string, std::vector<std::string>> y = zad1_c(data);
    y = zad1_e_2(y);
    for (auto [href, nbs] : y)
    {
        std::cout << href <<"\n";
        for (auto nb : nbs)
        {
            std::cout << "\t|____________ " << nb << "\n";
        }
        std::cout << "\n\n\n";
    }

    zad1_g(y);
    return 0;
}
*/
