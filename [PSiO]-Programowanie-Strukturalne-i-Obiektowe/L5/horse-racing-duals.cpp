#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int
main ()
{
  int N;
  vector<int> strengths;
  cin >> N;
  cin.ignore ();
  for (int i = 0; i < N; i++)
    {
      int Pi;
      cin >> Pi;
      cin.ignore ();
      strengths.push_back (Pi);
    }
  std::sort (strengths.begin (), strengths.end ());
  int lowest_diff = abs (strengths[1] - strengths[0]);
  for (int i = 1; i < strengths.size (); i++)
    {
      int diff = abs (strengths[i] - strengths[i - 1]);
      if (diff < lowest_diff)
        {
          lowest_diff = diff;
        }
    }

  cout << lowest_diff << endl;
}
