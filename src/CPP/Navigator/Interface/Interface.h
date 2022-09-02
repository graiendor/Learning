//
// Created by Emery Reva on 8/30/22.
//

#ifndef GRAPH__INTERFACE_H_
#define GRAPH__INTERFACE_H_

#include <filesystem>
#include <string>

#include "../Graph/graph.h"
#include "../GraphAlgorithms/GraphAlgorithms.h"
#include "ftxui/dom/elements.hpp"
#include "ftxui/screen/screen.hpp"
#include "ftxui/screen/string.hpp"

class Interface {
 public:
  void start();
 private:
  bool stop{false};

  auto initialization()             -> void;
  auto initialize_start_page()      -> void;
  auto initialize_load_file_page()  -> void;

  ftxui::Screen screen_                      {ftxui::Screen::Create(ftxui::Dimension::Full())};
  std::shared_ptr<ftxui::Node> start_page_   {};
  std::shared_ptr<ftxui::Node> load_page_    {};
  std::shared_ptr<ftxui::Node> load_result_  {};

  auto load_graph()                 -> void;

  Graph graph_{};
  GraphAlgorithms graph_algorithms_{};

//  ftxui::Element options;


};

#endif //GRAPH__INTERFACE_H_
