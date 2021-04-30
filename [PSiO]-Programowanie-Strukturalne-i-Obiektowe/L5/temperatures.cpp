#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    if(n==0) { cout<<0<<endl; return 0; }
    int closest=5527; // max temp+1

    while(n--)
    {
        int t;
        cin >> t; cin.ignore();

        if(abs(t)<=abs(closest))
            closest = t==-closest ? abs(t) : t;
    }

    cout << closest << endl;
    return 0;
}