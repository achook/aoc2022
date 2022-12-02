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
            auto myMove = line[2];

            points += myMove-87;

            
            if (opponentMove-'A' == myMove-'X'){
                // It's a draw
                points += 3;
            } else if ((opponentMove == 'A' && myMove == 'Y') ||
                       (opponentMove == 'B' && myMove == 'Z') || 
                       (opponentMove == 'C' && myMove == 'X')) {
                    points += 6;
            }

            totalPoints += points;
        }
    }

    file.close();
  }

  cout << "Total points: " << totalPoints << endl;

  return 0;
}