#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    // game loop
    while (1) {
        int tallest=0;
        int tallest_idx=0;
        for (int i = 0; i < 8; i++) {
            int mountainH;
            cin >> mountainH; cin.ignore();
            if(mountainH>tallest){
                tallest=mountainH;
                tallest_idx=i;
            }
        }

        cout << tallest_idx << endl; 
    }
    return 0;
}