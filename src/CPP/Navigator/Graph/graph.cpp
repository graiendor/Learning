//
// Created by Emery Reva on 8/13/22.
//

#include "graph.h"
void Graph::loadGraphFromFile(const std::string& filename) {
  std::ifstream file{filename};
  file >> size;
  int value{};
  for (int i {1}; i <= size; i++) {
    for (int j{1}; j <= size; j++) {
      value = 0;
      matrix_.emplace(i, std::vector<std::pair<int, int>>{});
      file >> value;
      matrix_[i].emplace_back(j, value);
    }
  }
//  for (auto& it : matrix_) {
//    std::cout << it.first << " : " << std::endl;
//    for (auto& iter : it.second) {
//      std::cout << iter.first << " : " << iter.second << " . ";
//    }
//    std::cout << std::endl;
//  }
  file.close();
}

void Graph::exportGraphToDot(const std::string& filename) const {
  std::ofstream file{filename};
  file << "Graph" << "graphname" << "{" << std::endl;
  for (int i {}; i < size; i++) {
    file << (char)('a' + i) << ";" << std::endl;
  }

  for (int i {1}; i < size; i++) {
    for (int j {1}; j < size; j++) {
      if (getConnectionValue(i, j)) {
        file << (char)('a' + i) << " -- " <<  (char)('a' + j) << std::endl;
      }
    }
  }
  file.close();
}

int Graph::getSize() const {
  return size;
}

int Graph::getConnection(const int& i, const int& j) const {
  return matrix_.at(i).at(j - 1).first;
}

int Graph::getConnectionValue(const int& i, const int& j) const {
  return matrix_.at(i).at(j).second;
}