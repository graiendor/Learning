#include <iostream>
#include "graph.h"

int main() {
  Graph graph{};
  std::cout << system("ls Testing");
  graph.loadGraphFromFile("graph.txt");
  graph.exportGraphToDot("graph_out.txt");
  return 0;
}
