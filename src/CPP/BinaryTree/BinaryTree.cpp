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

}

int main () {
  testing::InitGoogleTest();
  return RUN_ALL_TESTS();
//  BinaryTree tree {};

//  auto get = tree.push(3);
//  BinaryTree::Iterator iter{get.first};
//  ASSERT_EQ(iter->value, 3);
//  ASSERT_TRUE(get.second);
//  get = tree.push(2);
//  iter = get.first;
//  ASSERT_EQ(iter->value, 2);
//  ASSERT_TRUE(get.second);

//  ASSERT_EQ(iter->previous->left->value, 2);
//  ASSERT_EQ(iter->previous->value, 3);

//  get = tree.push(4);
//  iter = get.first;
//  ASSERT_EQ(iter->value, 4);
//  ASSERT_TRUE(get.second);

//  ASSERT_EQ(iter->previous->left->value, 2);
//  ASSERT_EQ(iter->previous->value, 3);
//
//  get = tree.push(8);
//  iter = get.first;
//  ASSERT_EQ(iter->value, 8);
//  ASSERT_TRUE(get.second);
}