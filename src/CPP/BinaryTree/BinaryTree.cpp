//
// Created by Emery Reva on 4/19/22.
//

#include "BinaryTree.h"
#include "gtest/gtest.h"

TEST(Map, basic) {
  BinaryTree tree {};

  auto get = tree.push(3);
  BinaryTree::Iterator iter{get.first};
  ASSERT_EQ(iter->value, 3);
  ASSERT_TRUE(get.second);
  get = tree.push(2);
  iter = get.first;
  ASSERT_EQ(iter->value, 2);
  ASSERT_TRUE(get.second);

  ASSERT_EQ(iter->previous->left->value, 2);
  ASSERT_EQ(iter->previous->value, 3);

  get = tree.push(4);
  iter = get.first;
  ASSERT_EQ(iter->value, 4);
  ASSERT_TRUE(get.second);

  ASSERT_EQ(iter->previous->left->value, 2);
  ASSERT_EQ(iter->previous->value, 3);

  get = tree.push(8);
  iter = get.first;
  ASSERT_EQ(iter->value, 8);
  ASSERT_TRUE(get.second);

  ASSERT_EQ(iter->previous->previous->value, 3);
  ASSERT_EQ(iter->previous->value, 4);

  tree.clear();

 get = tree.push(1);
 iter = get.first;
 ASSERT_EQ(iter->value, 1);

 get = tree.push(3);
 ASSERT_EQ(iter->right->value, 3);
 iter = get.first;
 ASSERT_EQ(iter->value, 3);
 ASSERT_EQ(iter->previous->value, 1);

 get = tree.push(2);
 ASSERT_EQ(iter->left->value, 2);
 iter = get.first;
 ASSERT_EQ(iter->value, 2);
 ASSERT_EQ(iter->previous->value, 3);

 get = tree.push(4);
 ASSERT_EQ(iter->previous->right->value, 4);
 iter = get.first;
 ASSERT_EQ(iter->value, 4);
 ASSERT_EQ(iter->previous->value, 3);

 get = tree.push(7);
 ASSERT_EQ(iter->right->value, 7);
 iter = get.first;
 ASSERT_EQ(iter->value, 7);
 ASSERT_EQ(iter->previous->value, 4);

 get = tree.push(5);
 ASSERT_EQ(iter->left->value, 5);
 iter = get.first;
 ASSERT_EQ(iter->value, 5);
 ASSERT_EQ(iter->previous->value, 7);

 get = tree.push(6);
 ASSERT_EQ(iter->right->value, 6);
 iter = get.first;
 ASSERT_EQ(iter->value, 6);
 ASSERT_EQ(iter->previous->value, 5);

 get = tree.push(-5);
 iter = get.first;
 ASSERT_EQ(iter->value, -5);
 ASSERT_EQ(iter->previous->value, 1);
 ASSERT_EQ(iter->previous->right->value, 3);

 get = tree.push(8);
 iter = get.first;
 ASSERT_EQ(iter->value, 8);
 ASSERT_EQ(iter->previous->value, 7);
 ASSERT_EQ(iter->previous->right->value, 8);


  auto vect = tree.preorderTraversal();


  for (auto it = vect.begin(); it < vect.end(); it++) {

    cout << *it << ' ';
  }
  cout << endl;

  vect = tree.inorderTraversal();
  for (auto it = vect.begin(); it < vect.end(); it++) {

    cout << *it << ' ';
  }
  cout << endl;

}

int main () {
  testing::InitGoogleTest();
  return RUN_ALL_TESTS();
}