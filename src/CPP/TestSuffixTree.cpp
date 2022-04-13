#include <gtest/gtest.h>
#include "SuffixTree.h"

TEST(Tree, basic) {
  SuffixTree tree("vnk2435kvabco8awkh125kjneytbcd12qjhb4abcd123xmnbqwnw4t");
  string needle = "abcd1234";
  int threshold = 3;

  cout << tree.search(needle, threshold) << endl;

//ASSERT_EQ("mece", tree.test_string());
//
//ASSERT_EQ(6, tree.test_root_length());
//ASSERT_EQ(1, tree.test_child_length());
//ASSERT_EQ(4, tree.test_child_child_length());




//ASSERT_TRUE(tree.search("enal"));
}

int main() {
  testing::InitGoogleTest();
  return RUN_ALL_TESTS();
}
