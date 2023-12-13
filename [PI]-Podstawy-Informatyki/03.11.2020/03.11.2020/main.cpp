// Example program
#include <iostream>

int turn = 0; // 0 - O | 1 - X
int moves = 0;
bool playing = true;
int tab[3][3] = {
    {-1, -1, -1}, {-1, -1, -1}, {-1, -1, -1}}; // 0 - O | 1 - X | -1 - none

void reset() {
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
      tab[i][j] = -1;

  playing = true;
  moves = 0;
}

void show() {
  std::cout << "\n";

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++)
      if (tab[i][j] == -1)
        std::cout << ". ";

      else if (tab[i][j] == 0)
        std::cout << "O ";

      else
        std::cout << "X ";

    std::cout << "\n";
  }
}

bool canMove(int x, int y) { return (tab[x][y] == -1); }

void end() {
  if (moves > 9)
    std::cout << "draw!";
  else
    std::cout << (turn == 0 ? "O" : "X") << " has won!";
}

bool won() {
  int winning[8][3][2] = {{{0, 0}, {0, 1}, {0, 2}}, {{1, 0}, {1, 1}, {1, 2}},
                          {{2, 0}, {2, 1}, {2, 2}},

                          {{0, 0}, {1, 0}, {2, 0}}, {{0, 1}, {1, 1}, {2, 1}},
                          {{0, 2}, {1, 2}, {2, 2}},

                          {{0, 0}, {1, 1}, {2, 2}}, {{0, 2}, {1, 0}, {2, 0}}};

  for (int i = 0; i < 8; i++) {
    bool temp = true;
    for (int j = 0; j < 3; j++) {
      int x = winning[i][j][0], y = winning[i][j][1];

      if (tab[x][y] != turn)
        temp = false;
    }

    if (temp)
      return true;
  }

  return false;
}

void buttonClick(int x, int y) {
  if (canMove(x, y)) {
    tab[x][y] = turn;
    moves++;

    if (won())
      playing = false;

    else {
      if (moves == 9) {
        moves++;
        playing = false;
      }

      turn = !turn;
    }

    show();
  }

  else {
    std::cout << "\ncant move there\n";
  }
}

int main() {
  show();
  while (playing) {
    int x, y;
    std::cout << (turn == 0 ? "O" : "X") << ", type in x and y:\n";
    std::cin >> x >> y;
    buttonClick(x, y);
  }
  end();
  return 0;
}
