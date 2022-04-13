//
// Created by Emery Reva on 4/10/22.
//

#ifndef SRC_CPP_SUFFIXTREE_H_
#define SRC_CPP_SUFFIXTREE_H_
#include <string>
#include <memory>
#include <iostream>

#define MAX_CHAR 256

using namespace std;

class SuffixTree {
 public:
  void setString(string input) {
    text = input;
    overallLength = text.length();
    remainingLength = overallLength;
    construct();
    cout << root.length;
    cout << root.children[1].length << endl;
//    cout << *root.begin;
    if (root.children[0].isLinked) {
      cout << *root.children[0].link->begin << *root.children[0].link->end;
    }
    cout << *root.children[3].begin << endl;
    cout << *root.children[2].link->begin << endl;
  }

  string test_string() {
    string res{*root.children[1].begin, *root.children[1].end, *root.children[1].link->begin, *root.children[1].link->end};
    return res;
  }

  size_t test_root_length() {
    return root.length;
  }

  size_t test_child_length() {
    return root.children[0].length;
  }

  size_t test_child_child_length() {
    return root.children[0].children[0].length;
  }

  bool search(string input) {
    bool found{false};
    string::iterator begin {input.begin()}, end{input.end()}, find{text.begin()};
    size_t position{};
    while (position < root.length) {
      find = root.children[0].begin;
      if (*begin == *find) {
        found = true;
        break;
      }
      position++;
    }
    if (found) {
      while (begin != end) {
        if (*begin != *find) {
          found = false;
          break;
        }
        begin++;
        find++;
      }
    }
    return found;
  }

 private:
  string text{};
  size_t overallLength{};
  size_t remainingLength{};
  bool needToLink {false};


  struct TreeNode {
    shared_ptr<TreeNode[]> children{};
    TreeNode* link{};
    string::iterator begin{};
    string::iterator end{};
    size_t length{};
    bool isEmpty{true};
    bool isLinked{false};
    bool hasChildren{false};
  };

  TreeNode root{};
  TreeNode* toLink{};

  void construct() {
    root.children.reset(new TreeNode[overallLength]);
    root.hasChildren = true;
    string::iterator begin {text.begin()}, end {text.end()};
    size_t edge{};
    for (; begin < end; begin++, edge++) {
      //  phase
      extension(root, edge, begin, end);
      remainingLength--;
    }
  }

  void extension(TreeNode& node, size_t edge, string::iterator& begin, string::iterator& end) {
    bool isInserted {true};
    for (size_t position = 0; position <= edge; position++) {
      //  extension
      if (node.children[position].isEmpty) {
        node.children[position].begin = begin;
        node.children[position].isEmpty = false;
        node.children[position].end = begin;
        node.children[position].length++;
      } else if (!node.children[position].hasChildren) {
        string::iterator found = checkRepeat(node.children[position].begin, node.children[position].end, *begin);
        if (found != node.children[position].end && found != end) {
          if (*(found + 1) != *(begin + 1) && (found + 1) != end) {

            constructNewNode(node.children[position], found);
            node.children[position].length = node.children[position].end - node.children[position].begin;
            if (needToLink) {
//              cout << position << " " << *node.children[position].begin << endl;
              toLink->link = &node.children[position];
              toLink->isLinked = true;
              toLink = &node.children[position];
              if (node.children[position].length == 0) {
                needToLink = false;
                toLink = nullptr;
              }
            } else if (node.children[position].length != 0) {
              needToLink = true;
              toLink = &node.children[position];
            }
            edge--;
            isInserted = false;
          }
        } else {
          node.children[position].end = begin;
          node.children[position].length++;
        }
      } else {
        isInserted = false;
        extension(node.children[position], remainingLength, begin, end);
      }
//      node.children[position].length++;
//      node.children[position].length = node.children[position].end - node.children[position].begin + 1;
    }
    if (isInserted) {
      node.length++;
    }
  }

  string::iterator checkRepeat(string::iterator begin, string::iterator end, char ch) {
    while (begin < end && *begin != ch) {
      begin++;
    }
    return begin;
  }

  void constructNewNode(TreeNode& node, string::iterator& found) {
    node.children.reset(new TreeNode[remainingLength]);
    node.children[0].length = node.length;
    node.children[0].end = node.end;
    node.end = found;
    found++;
    node.children[0].begin = found;
    node.children[0].isEmpty = false;
    node.hasChildren = true;
  }



  };

#endif //SRC_CPP_SUFFIXTREE_H_
