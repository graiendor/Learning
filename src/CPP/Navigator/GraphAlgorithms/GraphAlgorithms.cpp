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

void GraphAlgorithms::getShortestPathBetweenVertices(Graph &graph, int vertex1, int vertex2) {
  int size = graph.getSize(), node{}, previousNode {}, elements{};
  std::vector<double> distance (1, 0);
  std::vector<bool> visited(size, false);
  std::stack<int> path{};
  std::stack<int> previousNodes{};
  bool found {false};
  while (!found && elements < size) {
    node = 0;
    elements += 1;
    if (!visited[vertex1 - 1]) { path.emplace(vertex1); }
    distance.emplace_back(std::numeric_limits<double>::infinity());
    visited[vertex1 - 1] = true;
    for (int i{}; i < size; i++) {
      int value = graph.getConnectionValue(vertex1, i);
      if (value && !visited[i]) {
        if (i == vertex2 - 1) {
          path.emplace(vertex2);
          found = true;
          break;
        }
        if (value < distance.back()) {
          node = i + 1;
          distance.back() = value;
        }
      }
    }
    if (node) {
      previousNodes.emplace(vertex1);
      vertex1 = node;
    } else {
      vertex1 = previousNodes.top();
      elements -= 1;
      path.pop();
//      path.erase(path.end());
      previousNodes.pop();
    }

  }
  std::cout << found;
//  std::cout << getNearestNode(graph, vertex1).first << " : " << getNearestNode(graph, vertex1).second;
}

//std::pair<int, int> GraphAlgorithms::getNearestNode(const Graph &graph, const int currentNode) {
//  int size = graph.getSize(), node{}, distance{std::numeric_limits<int>::max()};
//  for (int i{}; i < size; i++) {
//    int value = graph.getConnectionValue(currentNode, i);
//    if (value) {
//      if (value < distance) {
//        node = i;
//        distance = value;
//      }
//    }
//  }
//  return std::make_pair(node, distance);
//}