#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

struct command
{
    string op;
    string arg1;
    string arg2;
    int val;
    bool visited;
};

int operation(string& op, int& a, int& b);
void process(int n, map<int, command>& cmds);
int get_val(string& arg, map<int, command>& cmds);

void process(int n, map<int, command>& cmds)
{
    if (cmds[n].op == "VALUE")
    {
        if (cmds[n].arg1[0] == '$')
        {
            int idx = stoi(cmds[n].arg1.substr(1));
            if (!cmds[idx].visited)
            {
                process(idx, cmds);
                cmds[idx].visited = true;
            }
            cmds[n].val = cmds[idx].val;

        }
        else
        {
            cmds[n].val = stoi(cmds[n].arg1);
        }
    }
    else
    {
        int a1 = get_val(cmds[n].arg1, cmds);
        int a2 = get_val(cmds[n].arg2, cmds);
        cmds[n].val = operation(cmds[n].op, a1, a2);
    }
}

int main()
{
    int N;
    cin >> N; cin.ignore();
    map<int, command> cmds;
    for (int i = 0; i < N; i++) {
        string op;
        string arg1;
        string arg2;
        cin >> op >> arg1 >> arg2;
        cmds.insert(pair<int, command>(i, { op,arg1,arg2,0,false }));
    }

    for (auto& [n, c] : cmds)
    {
        if (!c.visited)
        {
            process(n, cmds);
            c.visited = true;
        }
    }

    for (auto& [n, c] : cmds)
    {
        cout << c.val << endl;
    }
}

int get_val(string& arg, map<int, command>& cmds)
{
    int ret = 0;

    if (arg[0] == '$')
    {
        int idx = stoi(arg.substr(1));
        if (!cmds[idx].visited)
        {
            process(idx, cmds);
            cmds[idx].visited = true;
        }

        ret = cmds[idx].val;
    }

    else
    {
        ret = stoi(arg);
    }

    return ret;
}

int operation(string& op, int& a, int& b)
{
    int ret = 0;

    if (op == "ADD")
    {
        ret = a + b;
    }

    if (op == "SUB")
    {
        ret = a - b;
    }

    if (op == "MULT")
    {
        ret = a * b;
    }

    return ret;
}
