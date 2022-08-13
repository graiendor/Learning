//
// Created by Emery Reva on 8/13/22.
//

#ifndef LABYRINTH_MODEL_LABYRINTH_H_
#define LABYRINTH_MODEL_LABYRINTH_H_

#include <vector>
#include <iostream>
#include <numeric>
#include <random>

class Labyrinth {
 public:
  void createLabyrinth(int width, int height) {
    set.emplace_back(*new std::vector<int>(width));
    labyrinth_right.emplace_back(*new std::vector<int>(width));
    labyrinth_bottom.emplace_back(*new std::vector<int>(width));
    std::iota(set[0].begin(), set[0].end(), 1);
    init_labyrinth(width);
    add_bottom(width);
    for (int row{1}; row < height; row++) {
      labyrinth_right.emplace_back(*new std::vector<int>(width));
      labyrinth_bottom.emplace_back(*new std::vector<int>(labyrinth_bottom[row - 1]));
      set.emplace_back(*new std::vector<int>(set[row-1]));
      for (int labyrinth_index {}; labyrinth_index < width; labyrinth_index++) {
        if (labyrinth_bottom[row][labyrinth_index] == 1) {
          labyrinth_bottom[row][labyrinth_index] = 0;
          most_set += 1;
          set[row][labyrinth_index] = most_set;
        }
      }
    }




//      if (generate_random_number(0, 1)) {
//
//        if (set_count > 0 && labyrinth_index != width && set[0][labyrinth_index] != set[0][labyrinth_index + 1]) {
//          labyrinth_bottom[0][labyrinth_index] = 1;
//          isExit = false;
//        }
//      }
//      if (labyrinth_index != width && set[0][labyrinth_index] != set[0][labyrinth_index + 1]) {
//        set_count = 0;
//      } else {
//        set_count++;
//      }



    for (auto& i : labyrinth_right) {
      for (auto& j : i)
        std::cout << j;
      std::cout << std::endl;
    }
    std::cout << std::endl;
    for (auto& i : labyrinth_bottom) {
      for (auto& j : i)
        std::cout << j;
      std::cout << std::endl;
    }
    std::cout << std::endl;
    for (auto& i : set) {
      for (auto& j : i)
        std::cout << j;
      std::cout << std::endl;
    }


//    std::cout << labyrinth_right[0];
  }
 private:
  int generate_random_number(int from, int to);
  void init_labyrinth(int width);
  void add_bottom(int width);
  int most_set{};
  std::vector<std::vector<int>> labyrinth_right{};
  std::vector<std::vector<int>> labyrinth_bottom{};
  std::vector<std::vector<int>> set{};
};



#endif //LABYRINTH_MODEL_LABYRINTH_H_
