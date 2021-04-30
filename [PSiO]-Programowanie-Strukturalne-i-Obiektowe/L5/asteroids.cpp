#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct pos
{
    int x;
    int y;
};

pos get_pos_of_ast(char ast, vector<string> ast_map)
{
    for(int i=0; i<ast_map.size(); i++)
    {
        for(int j=0; j<ast_map[i].length(); j++)
        {
            if(ast_map[i][j] == ast)
            {
                return {j, i};
            }
        }
    }

    return {-1,-1};
}

ostream& operator<<(ostream& os, const pos& p)
{
    os << "{" << p.x << ", " << p.y << "}\n";
    return os;
}

int main()
{
    int w,h,t1,t2,t3;

    cin >> w >> h >> t1 >> t2 >> t3;

    vector<string> ast1;
    vector<string> ast2;

    for (int i = 0; i < h; i++) {
        string row1;
        string row2;

        cin >> row1 >> row2;

        ast1.push_back(row1);
        ast2.push_back(row2);
    }

    int dt12=t2-t1;
    int dt13=t3-t1;
    vector<string> opt(h, string(w,'.'));
    for(int i=0; i<ast1.size(); i++)
    {
        for(int j=0; j<ast1[i].length(); j++)
        {
            char ast=ast1[i][j];
            if(ast>='A' && ast<='Z')
            {
                pos t2_pos = get_pos_of_ast(ast, ast2);
                if(t2_pos.x == -1 && t2_pos.x == -1) {continue;}
                pos ddist = {t2_pos.x-j, t2_pos.y-i};
                float Vx=float(ddist.x)/dt12;
                float Vy=float(ddist.y)/dt12;
                //cerr<<Vx<<" "<<Vy<<endl;
                pos new_pos = {int(floor(j + Vx*dt13)), int(floor(i + Vy*dt13))};
                cerr<<ast<<":\ndt12="<<dt12<<"\nx1={"<<j<<", "<<i<<"}\nx2="<<t2_pos<<"dist=x2-x1="<<ddist<<"V={"<<Vx<<","<<Vy<<"}\nx3=x1+dist*V="<<new_pos<<endl;
                
                if(new_pos.x>=0 && new_pos.x<w && new_pos.y>=0 && new_pos.y<h)
                {
                    char* curr_ast = &opt[new_pos.y][new_pos.x];
                    if(*curr_ast=='.')
                    {
                        *curr_ast = ast;
                    }
                    else
                    {
                        *curr_ast = min(*curr_ast,ast);
                    }
                }
            }
        }
    }

    for(int i=0; i<opt.size(); i++)
    {
        cout<<opt[i]<<endl;
    }
}