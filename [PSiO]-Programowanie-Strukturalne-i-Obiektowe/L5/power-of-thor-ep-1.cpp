#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct pos {
    int x;
    int y;
};

string str_dir(pos dir)
{
    if(dir.x == 1 && dir.y == 1)
    {
        return "SE";
    }
    else if(dir.x == 1 && dir.y == -1)
    {
        return "NE";
    }
    else if(dir.x == 1 && dir.y == 0)
    {
        return "E";
    }
    else if(dir.x == -1 && dir.y == 1)
    {
        return "SW";
    }
    else if(dir.x == -1 && dir.y == -1)
    {
        return "NW";
    }
    else if(dir.x == -1 && dir.y == 0)
    {
        return "W";
    }
    else if(dir.x == 0 && dir.y == 1)
    {
        return "S";
    }
    else if(dir.x == 0 && dir.y == -1)
    {
        return "N";
    }
    else
    {
        return "";
    }
}

pos get_dir(pos a, pos b)
{
    int x=b.x-a.x;
    int y=b.y-a.y;

    if(x<0) x = -1;
    else if(x>0) x = 1;
    else x = 0;

    if(y<0) y = -1;
    else if(y>0) y = 1;
    else y = 0;

    return {x, y};
}

int main()
{
    int dest_x, dest_y, x, y; 
    cin >> dest_x >> dest_y >> x >> y;

    pos x1 = {x, y};
    pos x2 = {dest_x, dest_y};

    while (1) {
        int turns; cin >> turns; //ingore this

        pos dir = get_dir(x1, x2);
        cout<<str_dir(dir)<<endl;
        x1={x1.x + dir.x, x1.y + dir.y};
    }
}