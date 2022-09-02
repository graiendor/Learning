//
// Created by Emery Reva on 8/30/22.
//

#include "Interface.h"



int main() {
  Interface interface;
  interface.start();
}

void Interface::start() {
  using namespace ftxui;
  initialization();
  screen_ = Screen::Create(Dimension::Full(), Dimension::Fit(start_page_));
  Render(screen_, start_page_);
  std::cout << screen_.ToString() << '\0' << std::endl;
  run();
}

auto Interface::run() -> void {
  while (!stop) {
    int option{};
    std::cin >> option;
    screen_.Clear();
    switch (option) {
      case 1:
        load_graph();
        break;
      case 3:
        depth_search();
        break;
    }
  }
}

auto Interface::load_graph() -> void {
  using namespace ftxui;
  Render(screen_, load_page_);
  std::cout << screen_.ToString() << '\0' << std::endl;
  std::string path {};
  std::shared_ptr<ftxui::Node> load_result_ {};
  std::cin >> path;
  if (graph_.loadGraphFromFile(path)) {
    load_result_ = text(L" Загрузка графа прошла успешно ") | bold | color(Color::Green);
  } else {
    load_result_ = text(L" Указанного файла не существует ") | bold | color(Color::Red);
  }
  screen_.Clear();
  Render(screen_, start_page_);
  Render(screen_, load_result_);
  std::cout << std::endl << screen_.ToString() << '\0' << std::endl;
}

auto Interface::depth_search() -> void {
  using namespace ftxui;
  screen_.Clear();
  int size_ = graph_.getSize(), startVertex {};
  if (size_) {
    auto list = [&] {
      auto content = vbox({
                              text(L" Текущий размер графа:") | bold | color(Color::Green),
                              text(L" " + std::to_wstring(size_)) | bold | color(Color::Green),
                              text(L" Введите, пожалуйста, отправную точку:") | bold | color(Color::Green),
                          });
      return window(text(L" Обход графа в глубину "), content);
    };
    depth_page_ =  //
        vbox({
                 list(),
             });
    depth_page_ = depth_page_ | size(WIDTH, LESS_THAN, 80);
    Render(screen_, depth_page_);
    std::cout << std::endl << screen_.ToString() << '\0' << std::endl;
    std::cin >> startVertex;
    auto result = graph_algorithms_.depthFirstSearch(graph_, startVertex);

    std::string path {};
    while (!result.empty()) {
      path += (" " + std::to_string(result.top()));
      result.pop();
    }

//    std::reverse(path.begin(), path.end());

    auto list_after = [&] {
      auto content = vbox({
                              text(L" Текущий размер графа:") | bold | color(Color::Green),
                              text(L" " + std::to_wstring(size_)) | bold | color(Color::Green),
                              text(L" Обход завершен") | bold | color(Color::Green),
                              text(L" Полученный путь:")  | bold | color(Color::Green),
                              text(path) | bold | color(Color::Green)
                          });
      return window(text(L" Обход графа в глубину "), content);
    };

    depth_page_ =  //
        vbox({
                 list_after(),
             });
    depth_page_ = depth_page_ | size(WIDTH, LESS_THAN, 80);

//    graph_algorithms_.depthFirstSearch(graph_);
  } else {
    depth_page_ = text(L" Граф не загружен или пустой (как сделать обход пустоты?) ") | bold | color(Color::Red);
  }
  screen_.Clear();

  Render(screen_, depth_page_);
  std::cout << std::endl << screen_.ToString() << '\0' << std::endl;
  screen_.Clear();
  Render(screen_, start_page_);
}