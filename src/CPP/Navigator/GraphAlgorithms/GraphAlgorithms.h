//
// Created by Emery Reva on 8/14/22.
//

#ifndef NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_
#define NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_

#include "../Graph/graph.h"
#include <vector>
#include <queue>

class GraphAlgorithms {
 public:
  std::stack<int> depthFirstSearch(Graph &graph, int startVertex);
  std::queue<int> breadthFirstSearch(Graph &graph, int startVertex);
 private:


};

#endif //NAVIGATOR_GRAPHALGORITHMS_GRAPHALGORITHMS_H_
