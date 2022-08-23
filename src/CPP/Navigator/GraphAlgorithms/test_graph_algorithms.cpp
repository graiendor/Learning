//
// Created by Emery Reva on 8/15/22.
//

#include "../Graph/graph.h"
#include "GraphAlgorithms.h"

int main() {
  Graph graph("test1.txt");
  GraphAlgorithms algorithms{};
  auto vec = algorithms.depthFirstSearch(graph, 1);
  for (auto it {vec.begin()}; it < vec.end(); it++) {
    std::cout << *it << std::endl;
  }
}