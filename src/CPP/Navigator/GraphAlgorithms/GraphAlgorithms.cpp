//
// Created by Emery Reva on 8/14/22.
//

#include "GraphAlgorithms.h"
#include <algorithm>
#include <stack>
#include <vector>

std::stack<int> GraphAlgorithms::depthFirstSearch(Graph &graph, int startVertex) {
  std::stack<int> path {};
  std::stack<int> search {};
  bool connected {false};
  int size = graph.getSize();
  int elements {};
  std::vector<int> visited(size, 0);
  path.push(startVertex);
  search.push(startVertex);
  while (elements < size) {
    visited[path.top() - 1] = 1;
    elements += 1;
    connected = false;
    std::cout << startVertex << " \\ " << std::endl;
    for (int depth{}; depth < graph.getSize() && !connected; depth++) {
      std::cout << depth << " : ";
      if (graph.getConnectionValue(path.top(), depth) && !visited[depth]) {
        path.push(depth + 1);
        search.push(depth + 1);
        connected = true;
      }
    }
    if (!connected) {
      path.pop();
    }
    std::cout << "\nend" << std::endl;
  };
//  goToNext(graph, startVertex);
  return search;
}
