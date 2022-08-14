#include <iostream>
#include "graph.h"

int main() {
  Graph graph{};
  graph.loadGraphFromFile("graph.txt");
//  graph.exportGraphToDot("graph_out.txt");
  return 0;
}
