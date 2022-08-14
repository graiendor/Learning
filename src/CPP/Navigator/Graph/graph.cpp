//
// Created by Emery Reva on 8/13/22.
//

#include "graph.h"
void Graph::loadGraphFromFile(const std::string& filename) {
  std::ifstream file{filename};
  file >> size;
  int value{};
  for (int i {1}; i < size; i++) {
    for (int j{1}; j < size; j++) {
      nodes.emplace(i, std::vector<std::pair<int, int>>{});
      file >> value;
      if (value) {
        nodes[i].emplace_back(j, value);
      }
    }
  }
  for (auto& it : nodes) {
    std::cout << it.first << " : " << std::endl;
    for (auto& iter : it.second) {
      std::cout << iter.first << " : " << iter.second << " . ";
    }
    std::cout << std::endl;
  }

//  matrix.resize(size);
//  for (int i{}; i < size; i++) {
//    matrix[i].resize(size);
//  }
//  for (auto& i : matrix) {
//    for (auto& j : i) {
//      file >> j;
//    }
//  }
//
//  for (auto& i : matrix) {
//    for (auto& j : i) {
//      std::cout << j << " ";
//    }
//    std::cout << std::endl;
//  }
  file.close();
}

void Graph::exportGraphToDot(const std::string& filename) {
  std::ofstream file{filename};
//  file << "Graph" << "graphname" << "{" << std::endl;
//  for (int i {}; i < size; i++) {
//    file << (char)('a' + i) << ";" << std::endl;
//  }
//
//  for (int i {}; i < size; i++) {
//    for (int j {}; j < size; j++) {
//      if (matrix[i][j]) {
//        file << (char)('a' + i) << " -- " <<  (char)('a' + j) << std::endl;
//      }
//    }
//  }
  file.close();
}

int Graph::getSize() const {
  return size;
}
int Graph::getNode(const int& i, const int& j) const {
  return 1;
//  return matrix[i][j];
}
