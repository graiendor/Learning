//
// Created by Emery Reva on 8/15/22.
//

#include "../Graph/graph.h"
#include "GraphAlgorithms.h"

int main() {
  Graph graph("test1.txt");
  GraphAlgorithms algorithms{};
//  auto vec = algorithms.depthFirstSearch(graph, 1);
//  while (!vec.empty()) {
//    std::cout << vec.top() << std::endl;
//    vec.pop();
//  }

//  auto q = algorithms.breadthFirstSearch(graph, 1);
//  while (!q.empty()) {
//    std::cout << q.front() << std::endl;
//    q.pop();
//  }
  Graph graph_1("test2.txt");
  algorithms.getShortestPathBetweenVertices(graph_1, 1, 5);
}