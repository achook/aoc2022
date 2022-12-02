#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
  string line;
  ifstream file ("input.txt");

  auto totalPoints = 0;

  if (file.is_open()) {
   
    while (getline (file, line)) {
        if (line.length() == 3) {
            auto points = 0;

            auto opponentMove = line[0];
            auto result = line[2];

            // We need to lose
            if (result == 'X') {
                if (opponentMove == 'A') {
                    // The opponent plays rock, so we play scissors 
                    points += 3;
                } else if (opponentMove == 'B') {
                    // The opponent plays paper, so we play rock
                    points += 1;
                } else if (opponentMove == 'C') {
                    // The opponent plays scissors, so we play paper
                    points += 2;
                }
            // We need to draw
            } else if (result == 'Y') {
                points += 3;
                points += opponentMove - 'A' + 1;
            // We need to win
            } else if (result == 'Z') {
                points += 6;
                if (opponentMove == 'A') {
                    // The opponent plays rock, so we play paper
                    points += 2;
                } else if (opponentMove == 'B') {
                    // The opponent plays paper, scissors
                    points += 3;
                } else if (opponentMove == 'C') {
                    // The opponent plays scissors, so we play rock
                    points += 1;
                }
            }

            totalPoints += points;
        }
    }

    file.close();
  }

  cout << "Total points: " << totalPoints << endl;

  return 0;
}