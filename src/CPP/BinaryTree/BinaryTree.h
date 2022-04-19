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

class BinaryTree {

 private:
  struct TreeNode {
    int value {};
    unique_ptr<TreeNode> left{};
    unique_ptr<TreeNode> right{};
    TreeNode *previous{nullptr};
    bool empty {true};
    bool isChecked {};
  };
  TreeNode root{};



 public:

  using Iterator = TreeNode*;

  std::pair<Iterator, bool> push(const int& value) {
    Iterator iterator {findToInsert(value)};
    auto result = insert(value, iterator);
    return result;
  }

  void clear() {
    root.empty = true;
    root.value = 0;
    root.left.reset();
    root.right.reset();
  }

  vector<int> preorderTraversal() {
    vector<int> result {};
    Iterator iterator {&root};
    bool toCheck {!iterator->isChecked}, notTotallyChecked {true};
    if (!iterator->empty) {
      result.push_back(iterator->value);
      iterator->isChecked = toCheck;
      do {
        if (!iterator->left->empty && iterator->left->isChecked != toCheck) {
          iterator = iterator->left.get();
          result.push_back(iterator->value);
          iterator->isChecked = toCheck;
        } else if (!iterator->right->empty && iterator->right->isChecked != toCheck){
          iterator = iterator->right.get();
          result.push_back(iterator->value);
          iterator->isChecked = toCheck;
        } else if (iterator->previous) {
          iterator = iterator->previous;
        } else {
          notTotallyChecked = false;
        }
      } while (notTotallyChecked);

    }
    return result;
  }

  vector<int> inorderTraversal() {
    vector<int> result {};
    Iterator iterator {&root};
    bool toCheck {!iterator->isChecked}, notTotallyChecked {true};
    if (!iterator->empty) {
      do {
        if (!iterator->left->empty && iterator->left->isChecked != toCheck) {
          iterator = iterator->left.get();
//          result.push_back(iterator->value);
//          iterator->isChecked = toCheck;
        } else if (!iterator->right->empty && iterator->right->isChecked != toCheck) {
          if (iterator->isChecked != toCheck) {
            result.push_back(iterator->value);
            iterator->isChecked = toCheck;
          }
          iterator = iterator->right.get();
          result.push_back(iterator->value);
          iterator->isChecked = toCheck;
        } else if (iterator->previous) {
          if (iterator->isChecked != toCheck) {
            result.push_back(iterator->value);
            iterator->isChecked = toCheck;
          }
          iterator = iterator->previous;
        } else {
          notTotallyChecked = false;
        }
      } while (notTotallyChecked);

    }
    return result;
  }

 private:
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

  Iterator findToInsert(const int& value) {
    Iterator iterator {&root};
    bool found {false};
    while (!iterator->empty && !found) {
      if (value < iterator->value) {
        if (iterator->left->empty) {
          found = true;
        } else {
          iterator = iterator->left.get();
        }
      } else if (value > iterator->value) {
        if (iterator->right->empty) {
          found = true;
        } else {
          iterator = iterator->right.get();
        }
      }
    }
    return iterator;
  }

};


#endif //SRC_CPP_BINARY_TREE_BINARYTREE_H_
