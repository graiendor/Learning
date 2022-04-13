#include "SuffixTree.h"
#include <chrono>

int main() {
  std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

  SuffixTree tree("vnk2435kvabco8awkh125kjneytbcd12qjhb4acd123xmnbqwnw4tq");
  std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
  std::cout << "Exit = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
  string needle = "abcd1234";
  int threshold = 3;

  cout << tree.search(needle, threshold) << endl;
}