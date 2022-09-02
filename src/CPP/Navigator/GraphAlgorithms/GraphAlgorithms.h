//
// Created by Emery Reva on 8/14/22.
//

#ifndef NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_
#define NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_

#include "../Graph/graph.h"
#include <vector>
#include <queue>
#include <stack>

class GraphAlgorithms {
 public:
  std::stack<int> depthFirstSearch(Graph &graph, int startVertex);
  std::queue<int> breadthFirstSearch(Graph &graph, int startVertex);
  void getShortestPathBetweenVertices(Graph &graph, int vertex1, int vertex2);
 private:

//  std::pair<int, int> getNearestNode(const Graph &graph, int currentNode);
};

#endif //NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_
