//
// Created by Emery Reva on 8/13/22.
//

#include "Labyrinth.h"

int Labyrinth::generate_random_number(const int from, const int to) {
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<> distr(from, to);
  return distr(gen);
}

void Labyrinth::init_labyrinth(const int width) {
  int last_index {};
  for (int labyrinth_index {}; labyrinth_index < width; labyrinth_index++) {
    if (generate_random_number(0, 1)) {
      labyrinth_right[0][labyrinth_index] = 1;
      set[0][labyrinth_index] = set[0][last_index];
      last_index = labyrinth_index + 1;
    } else {
      set[0][labyrinth_index] = set[0][last_index];
    }
  }
  labyrinth_right[0][width - 1] = 1;
  most_set = set[0][width - 1];
}

void Labyrinth::add_bottom(int width) {
  bool isExit{false};
  for (int labyrinth_index {}; labyrinth_index < width; labyrinth_index++) {
    if (!generate_random_number(0, 1)) {
      isExit = true;
    } else if (!(!isExit && labyrinth_right[0][labyrinth_index] == 1)) {
      labyrinth_bottom[0][labyrinth_index] = 1;
    }
    if (labyrinth_right[0][labyrinth_index] == 1) isExit = false;
  }
}
