//
// Created by Emery Reva on 4/19/22.
//

#ifndef SRC_CPP_BINARY_TREE_BINARYTREE_H_
#define SRC_CPP_BINARY_TREE_BINARYTREE_H_

#include <memory>
#include <vector>
#include <memory>
#include <iostream>

using std::cout;
using std::endl;

using std::vector;
using std::unique_ptr;

/**
 * Definition for a binary tree node.

 */
class Solution {

};

class BinaryTree {

 private:
  struct TreeNode {
    int value {};
    unique_ptr<TreeNode> left{};
    unique_ptr<TreeNode> right{};
    TreeNode *previous{};
    bool empty {true};
  };
  TreeNode root{};



 public:

  using Iterator = TreeNode*;

  std::pair<Iterator, bool> push(const int& value) {
    Iterator iterator {&root};
    iterator = find(value);
    auto result = insert(value, iterator);
    return result;
  }

  static std::pair<Iterator, bool> insert(const int& value, Iterator iterator) {
    bool isPushed {false};
    if (iterator->empty) {
      createNode(value, iterator);
      isPushed = true;
    } else {
      if (value < iterator->value) {
        iterator->left->previous = iterator;
        iterator = iterator->left.get();
        createNode(value, iterator);
        isPushed = true;
      } else if (value > iterator->value) {
        iterator->right->previous = iterator;
        iterator = iterator->right.get();
        createNode(value, iterator);
        isPushed = true;
      }
    }
    return std::make_pair(iterator, isPushed);
  }

  static void createNode(const int& value, const Iterator& iterator) {
    iterator->value = value;
    iterator->empty = false;
    iterator->left = std::make_unique<TreeNode>();
    iterator->right = std::make_unique<TreeNode>();
  }

  Iterator find(const int& value) {
    Iterator iterator {&root};
    while (!iterator->empty && !iterator->left->empty && !iterator->right->empty) {
      if (value < iterator->value) {
        iterator = iterator->left.get();
      } else if (value > iterator->value) {
        iterator = iterator->right.get();
      }
    }
    return iterator;
  }
};

//  vector<int> preorderTraversal(TreeNode* root) {
//    vector<int> result {};
//    TreeNode* iter {root};
//    result.push_back(iter->val);
//    while (iter->left != nullptr) {
//      result.push_back(iter->val);
//      iter = iter->left;
//    }
//    iter = root;
//    while (iter->right != nullptr) {
//      result.push_back(iter->val);
//      iter = iter->right;
//    }
//  }
//};

#endif //SRC_CPP_BINARY_TREE_BINARYTREE_H_
