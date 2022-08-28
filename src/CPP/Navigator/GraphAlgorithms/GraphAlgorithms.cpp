//
// Created by Emery Reva on 8/14/22.
//

#include "GraphAlgorithms.h"
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>

std::stack<int> GraphAlgorithms::depthFirstSearch(Graph &graph, int startVertex) {
  std::stack<int> path {};
  std::stack<int> search {};
  int size = graph.getSize();
  int elements {};
  std::vector<int> visited(size, 0);
  path.push(startVertex);
  search.push(startVertex);
  while (elements < size) {
    visited[path.top() - 1] = 1;
    elements += 1;
    bool connected {false};
    for (int depth{}; depth < size && !connected; depth++) {
      if (graph.getConnectionValue(path.top(), depth) && !visited[depth]) {
        path.push(depth + 1);
        search.push(depth + 1);
        connected = true;
      }
    }
    if (!connected) {
      path.pop();
    }
  };
  return search;
}

std::queue<int> GraphAlgorithms::breadthFirstSearch(Graph &graph, int startVertex) {
  std::queue<int> search {};
  std::queue<int> toVisit {};
  int size = graph.getSize(), elements{};
  toVisit.push(startVertex);
  std::vector added(size, 0);
  while (!toVisit.empty()) {
    int vertex = toVisit.front();
    search.push(vertex);
    added[vertex - 1] = 1;
    toVisit.pop();
    elements += 1;
    for (int breadth{}; breadth < size; breadth++) {
      if (graph.getConnectionValue(vertex, breadth) && !added[breadth]) {
        toVisit.push(breadth + 1);
        added[breadth] = 1;
      }
    }
  }
  return search;
}