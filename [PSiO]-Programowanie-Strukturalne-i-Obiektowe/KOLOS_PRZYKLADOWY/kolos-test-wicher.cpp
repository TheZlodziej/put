#include <SFML/Graphics.hpp>
#include <iostream>

class AvengerSprite : public sf::Sprite
{
public:
    enum TYP {Thor, Kamien, Stwor};

    sf::Vector2f szybkosc;
    TYP typ;

    AvengerSprite(sf::Texture* tekstura) :sf::Sprite(), szybkosc(0.0f, 0.0f)
    {
        setTexture(*tekstura);
        scale(0.1f, 0.1f);
        setOrigin(getGlobalBounds().width * 0.5f, getGlobalBounds().height * 0.5f);
    }

    virtual ~AvengerSprite()
    {
    }

    bool Kolizja(AvengerSprite* postac)
    {
        return getGlobalBounds().intersects(postac->getGlobalBounds());
    }

    void Pokaz(sf::RenderWindow& okno)
    {
        okno.draw(*this);
    }

    void Animuj(const sf::Time& elapsed)
    {
        move(szybkosc * elapsed.asSeconds());
        
        sf::FloatRect pr = getGlobalBounds();
        sf::Vector2f p = getPosition();

        if (p.x - pr.width * 0.5f > 1000.0f)
        {
            setPosition(-pr.width * 0.5f, p.y);
        }
        
        else if (p.x + pr.width * 0.5f < 0.0f)
        {
            setPosition(1000.0f + pr.width * 0.5f, p.y);
        }

        if (p.y + pr.height * 0.5f < 0.0f)
        {
            setPosition(p.x, 1000.0f + pr.height * 0.5f);
        }

        else if (p.y - pr.height * 0.5f > 1000.0f)
        {
            setPosition(p.x, -pr.height * 0.5f);
        }

    }
};

class Thor : public AvengerSprite
{
private:
    int m_zycia;
    int m_punkty;

public:
    Thor(sf::Texture* tekstura) : AvengerSprite(tekstura), m_zycia(3), m_punkty(0)
    {
        szybkosc = sf::Vector2f(150.0f, 0.0f);
        typ = AvengerSprite::TYP::Thor;
    }

    virtual ~Thor()
    {
    }

    int Zycia() const { return m_zycia; }
    int Punkty() const { return m_punkty; }

    void OdejmijZycie() { m_zycia--; }
    void DodajPuntky(const int& pkt) { m_punkty += pkt; }
};

class KamienNieskonczonosci : public AvengerSprite
{
public:
    KamienNieskonczonosci(sf::Texture* tekstura) : AvengerSprite(tekstura)
    {
        szybkosc = sf::Vector2f(0.0f, 50.0f);
        typ = AvengerSprite::TYP::Kamien;
    }

    virtual ~KamienNieskonczonosci()
    {
    }

    void Powieksz()
    {
        sf::Vector2f teraz_skala = getScale();
        if (teraz_skala.x < .8f && teraz_skala.y < .8f)
        {
            setScale(teraz_skala * 2.0f);
        }
    }

};

class StworOutrider : public AvengerSprite
{
public:
    StworOutrider(sf::Texture* tekstura) : AvengerSprite(tekstura)
    {
        typ = AvengerSprite::TYP::Stwor;
        bool lewo = rand() % 2;
        if (lewo)
        {
            szybkosc = sf::Vector2f(-100.0f, 0.0f);
        }
        else
        {
            szybkosc = sf::Vector2f(100.0f, 0.0f);
        }
    }

    virtual ~StworOutrider()
    {
    }
};

void umiesc_w_losowym_miejscu(AvengerSprite* postac, sf::Vector2f minmax)
{
    float losowe_x = rand() % (int)(minmax.x);
    float losowe_y = rand() % (int)(minmax.y);
    postac->setPosition(losowe_x, losowe_y);
}

int main()
{
    sf::RenderWindow okno(sf::VideoMode(1000.0f, 1000.0f), "kolos wicher");

    // tekstury //

    std::map<std::string, sf::Texture*> tekstury;

    tekstury.insert(std::make_pair("kamien", new sf::Texture()));
    tekstury.insert(std::make_pair("thor", new sf::Texture()));
    tekstury.insert(std::make_pair("stwor", new sf::Texture()));

    tekstury["kamien"]->loadFromFile("tekstury/kamien.png");
    tekstury["thor"]->loadFromFile("tekstury/thor.png");
    tekstury["stwor"]->loadFromFile("tekstury/alien.png");

    // sprajty //

    std::vector<AvengerSprite*> postacie;
        
    Thor* thor = new Thor(tekstury["thor"]);
    postacie.emplace_back(thor);

    for (int i = 0; i < 20; i++)
    {
        StworOutrider* stwor = new StworOutrider(tekstury["stwor"]);
        umiesc_w_losowym_miejscu(stwor, sf::Vector2f(1000.0f, 1000.0f));
        postacie.emplace_back(stwor);
    }

    for (int i = 0; i < 6; i++)
    {
        KamienNieskonczonosci* kamien = new KamienNieskonczonosci(tekstury["kamien"]);
        umiesc_w_losowym_miejscu(kamien, sf::Vector2f(1000.0f, 1000.0f));
        postacie.emplace_back(kamien);
    }
 
    
    // postacie setup //

    sf::Vector2f srodek_okna = sf::Vector2f(1000.0f, 1000.0f) * 0.5f;
    postacie[0]->setPosition(srodek_okna); // 0 to thor

    // glowna petla //

    sf::Clock zegar;
    sf::Time czas_teraz;
    bool klikniecie_mysza = true;

    while (okno.isOpen())
    {
        sf::Event event;
        while (okno.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                okno.close();
        }

        // input z myszki

        if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
        {
            if (klikniecie_mysza)
            {
                klikniecie_mysza = false;
                sf::Vector2i pozycja_i = sf::Mouse::getPosition(okno);
                sf::Vector2f pozycja_f((float)pozycja_i.x, (float)pozycja_i.y);

                for (auto& postac : postacie)
                {
                    if (postac->typ != AvengerSprite::TYP::Kamien) { continue; }

                    KamienNieskonczonosci* kamien = static_cast<KamienNieskonczonosci*>(postac);

                    sf::FloatRect poz = kamien->getGlobalBounds();
                    if (
                        pozycja_f.x >= poz.left &&
                        pozycja_f.x <= poz.left + poz.width &&
                        pozycja_f.y >= poz.top &&
                        pozycja_f.y <= poz.top + poz.height
                        )
                    {
                        kamien->Powieksz();
                    }
                }
            }   
        }
        else
        {
            klikniecie_mysza = true;
        }

        // input z klawiatury
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::A))
        {
            postacie[0]->szybkosc = sf::Vector2f(-150.0f, 0.0f);
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::W))
        {
            postacie[0]->szybkosc = sf::Vector2f(0.0f, -150.0f);
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::S))
        {
            postacie[0]->szybkosc = sf::Vector2f(0.0f, 150.0f);
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::D))
        {
            postacie[0]->szybkosc = sf::Vector2f(150.0f, 0.0f);
        }

        // rysowanie
        czas_teraz = zegar.restart();

        okno.clear(sf::Color::White);

        for (auto& postac : postacie)
        {
            postac->Animuj(czas_teraz);
            postac->Pokaz(okno);
        }

        okno.display();

        // kolizje //

        Thor* thor = static_cast<Thor*>(postacie[0]);

        auto postac = postacie.begin() + 1;
        
        while (postac != postacie.end())
        {
            if (thor->Kolizja(*postac))
            {
                if ((*postac)->typ == AvengerSprite::TYP::Kamien)
                {
                    thor->DodajPuntky(100);
                }
                else if ((*postac)->typ == AvengerSprite::TYP::Stwor)
                {
                    thor->OdejmijZycie();
                }

                postac = postacie.erase(postac);
                thor->setPosition(srodek_okna);
            }

            else
            {
                ++postac;
            }
        }

        // warunki koncowe //

        if (thor->Zycia() == 0)
        {
            std::cout << "PRZEGRANA";
            okno.close();
        }

        if (thor->Punkty() == 600)
        {
            std::cout << "WYGRANA";
            okno.close();
        }
    }

    // zwalnianie pamieci //

    for (auto& [k, tekstura] : tekstury)
    {
        delete tekstura;
    }

    for (auto& postac : postacie)
    {
        delete postac;
    }

    return 0;
}