#include <SFML/Graphics.hpp>

class TrapezeShape : public sf::ConvexShape
{
public:
    float a;
    float b;
    sf::Vector2f bl;

    TrapezeShape(float pos_x, float pos_y, sf::Vector2f tl, sf::Vector2f br, float a, float b): a(a), b(b), ConvexShape()
    {
        setPointCount(4);
        float x = br.x - b / 2.0f;
        float y = br.y;

        sf::Vector2f tr(tl.x+a, tl.y);
        bl = sf::Vector2f(br.x-b, br.y);

        setPoint(0, tl);
        setPoint(1, tr);
        setPoint(2, br);
        setPoint(3, bl);

        //origin podstawa dolna srodek
        setOrigin(x, y);
        setPosition(pos_x, pos_y);
        setFillColor(sf::Color::Red);
    }

    virtual ~TrapezeShape()
    {
    
    }
};

int main()
{
    sf::RenderWindow window(sf::VideoMode(1000, 1000), "TEST");
    sf::Clock timer;
    float time_elapsed=0.0f;
    std::vector<TrapezeShape> traps;
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        time_elapsed += timer.restart().asSeconds();

        //if (time_elapsed > .01f)
        {  
            time_elapsed = 0.0f;

            sf::Vector2i mpos = sf::Mouse::getPosition(window);
            float mx = float(mpos.x);
            float my = float(mpos.y);

            if (traps.size() > 0)
            {
                TrapezeShape lastTrap = traps[traps.size() - 1];
                float a = lastTrap.b;
                float b = a * 0.9f;

                if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
                {
                    a = 20.0f;
                    b = 20.0f;
                }

                sf::Vector2f tl = lastTrap.bl;
                sf::Vector2f br(mx + b / 2.0f, my);
                traps.emplace_back(mx, my, tl, br, a, b);
            }
            else
            {
                traps.emplace_back(mx, my, sf::Vector2f(mx,my), sf::Vector2f(mx,my), 30.0f, 30.0f);
            }
            
            if (traps.size() > 500)
            {
                traps.begin() = traps.erase(traps.begin());
            }
        }

        window.clear();

        for (auto& t : traps)
        {
            window.draw(t);
        }

        window.display();
    }

    return 0;
}