//
// Created by Emery Reva on 8/15/22.
//

#include "../Graph/graph.h"
#include "GraphAlgorithms.h"

int main() {
  Graph graph("test1.txt");
  GraphAlgorithms algorithms{};
  algorithms.depthFirstSearch(graph, 1);
}