//
// Created by Emery Reva on 8/14/22.
//

#include "GraphAlgorithms.h"
#include <algorithm>
#include "../libs/s21_containerAdaptor.h"

std::vector<int> GraphAlgorithms::depthFirstSearch(Graph &graph, int startVertex) {
  if (visited_.size() == graph.getSize()) { visited_.clear(); }
  goToNext(graph, startVertex);
  return visited_;
}
void GraphAlgorithms::goToNext(Graph &graph, int startVertex) {
  int size {graph.getSize()};
  visited_.emplace_back(startVertex);
  for (int i{1} ; i < size; i++) {
    std::cout << startVertex << " : " << i << " : " << graph.getConnectionValue(startVertex, i) << std::endl;
    if (std::find(visited_.begin(), visited_.end(), i) == visited_.end() && graph.getConnectionValue(startVertex, i)) {
      goToNext(graph, i);
    }
  }
}