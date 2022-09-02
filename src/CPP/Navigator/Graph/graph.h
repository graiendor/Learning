//
// Created by Emery Reva on 8/13/22.
//

#ifndef NAVIGATOR__GRAPH_H_
#define NAVIGATOR__GRAPH_H_

#include <vector>
#include <map>
#include <fstream>
#include <string>
#include <iostream>

class Graph {
 public:
  Graph() = default;;
  explicit Graph(const std::string& filename) {
    loadGraphFromFile(filename);
  }
  auto loadGraphFromFile(const std::string& filename) -> bool;
  void exportGraphToDot(const std::string& filename) const;
  [[nodiscard]] int getConnection(const int& i, const int& j) const;
  [[nodiscard]] int getConnectionValue(const int& i, const int& j) const;
  [[nodiscard]] int getSize() const;


 private:
  std::map<int, std::vector<std::pair<int, int>>> matrix_{};
  int size{};

};

#endif //NAVIGATOR__GRAPH_H_
