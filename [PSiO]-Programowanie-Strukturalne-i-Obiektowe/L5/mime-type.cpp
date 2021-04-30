#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

void lowercase(string& str)
{
    for(auto& c:str)
    {
        if(c>='A' && c<='Z')
        {
            c+= 'a' - 'A';
        }
    }
}

int main()
{
    int N; 
    cin >> N; cin.ignore();
    int Q;
    cin >> Q; cin.ignore();
    unordered_map<string, string> mimes;
    for (int i = 0; i < N; i++) {
        string EXT; 
        string MT;
        cin >> EXT >> MT; cin.ignore();
        lowercase(EXT);
        mimes.insert(pair<string, string>("."+EXT,MT));

    }

    for (int i = 0; i < Q; i++) {
        string FNAME;
        getline(cin, FNAME);

        lowercase(FNAME);
        reverse(FNAME.begin(), FNAME.end());
        string ext = FNAME.substr(0,FNAME.find(".")+1);
        reverse(ext.begin(), ext.end());

        if(mimes.find(ext)!=mimes.end())
        {
            cout<<mimes[ext]<<endl;
        }
        else
        {
            cout << "UNKNOWN" << endl;
        }
    }
}