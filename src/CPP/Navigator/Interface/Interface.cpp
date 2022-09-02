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
  while(!stop) {
    int option {};
    std::cin >> option;
    screen_.Clear();
    switch (option) {
      case 1:
        Render(screen_, load_page_);
        std::cout << screen_.ToString() << '\0' << std::endl;
        load_graph();
    }
  }
}
auto Interface::initialization() -> void {
  using namespace ftxui;
  initialize_start_page();
  initialize_load_file_page();


}
auto Interface::initialize_start_page() -> void {
  using namespace ftxui;
  auto options = [&] {
    auto content = vbox({
                            hbox({text(L"- 1. "), text(L"Загрузка исходного графа из файла") | bold}) | color(Color::Green),
                            hbox({text(L"- 2. "), text(L"Cоздание png файла (graphViz)") | bold}) | color(Color::Yellow),
                            hbox({text(L"- 3. "), text(L"Обход графа в ширину") | bold}) | color(Color::Green),
                            hbox({text(L"- 4. "), text(L"Обход графа в глубину") | bold}) | color(Color::Green),
                            hbox({text(L"- 5. "), text(L"Поиск кратчайшего пути между произвольными двумя вершинами") | bold}) | color(Color::Green),
                            hbox({text(L"- 6. "), text(L"Поиск кратчайших путей между всеми парами вершин в графе") | bold}) | color(Color::Red),
                            hbox({text(L"- 7. "), text(L"Поиск минимального остовного дерева в графе") | bold}) | color(Color::Red),
                            hbox({text(L"- 8. "), text(L"Решение задачи комивояжера") | bold}) | color(Color::Red),
                        });
    return window(text(L" Меню "), content);
  };
  start_page_ =  //
      vbox({
               options(),
           });
  start_page_ = start_page_ | size(WIDTH, LESS_THAN, 80);
}
auto Interface::initialize_load_file_page() -> void {
  using namespace ftxui;
  auto list = [&] {
    auto content = vbox({
                            text(L" Введите, пожалуйста, полный или относительный путь к файлу") | bold | color(Color::Green),
                            text(L" Текущий путь:")  | bold | color(Color::Green),
                            text(std::filesystem::current_path().wstring()) | color(Color::Yellow)
                        });
    return window(text(L" Загрузка исходного графа из файла "), content);
  };
  load_page_ =  //
      vbox({
               list(),
           });
  load_page_ = load_page_ | size(WIDTH, LESS_THAN, 80);

}
auto Interface::load_graph() -> void {
  using namespace ftxui;
  std::string path {};
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

