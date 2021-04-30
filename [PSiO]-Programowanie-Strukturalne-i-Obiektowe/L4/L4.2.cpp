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
