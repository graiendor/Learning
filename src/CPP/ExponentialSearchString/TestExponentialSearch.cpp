#include "ExponentialSearch.h"

int main() {
  string hayStack = "vnk2435kvabco8awkh125kjneytbcd12qjhb4abcd123xmnbqwnw4t";
  string needle = "abcd1234";

  list result(needleSearch(hayStack, needle, 3));
  size_t length = result.size();
  for (size_t iteration{}; iteration < length; iteration++) {
    auto res = result.front();
    result.pop_front();
    std::cout << "sequence of length = " << res.second - res.first + 1
              << " found at haystack offset " << distance(hayStack.begin(), res.first) << " needle offset " << iteration << std::endl;
  }
}