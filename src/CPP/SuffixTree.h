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
    construct();
  }

 private:
  string text{};
  size_t overallLength{};

  struct TreeNode {
    shared_ptr<TreeNode[]> children{};
    shared_ptr<TreeNode> link{};
    string::iterator begin{};
    string::iterator end{};
    size_t length{};
    bool isEmpty{true};
    bool hasChildren{false};
  };

  TreeNode root{};

  void construct() {
    root.children.reset(new TreeNode[overallLength]);
    root.hasChildren = true;
    string::iterator begin = text.begin(), end = text.end();
    size_t edge{};
    for (; begin < end; begin++, edge++) {
      //  phase
      extension(root, edge, begin, end);
    }
    cout << *root.children[3].begin << endl;
    cout << *root.children[3].end << endl;

    cout << *root.children[1].children[1].begin << endl;
    cout << *root.children[1].children[1].end << endl;
  }

  void extension(TreeNode& node, size_t edge, string::iterator& begin, string::iterator& end) {
    for (size_t position = 0; position <= edge; position++) {
      //  extension
      if (node.children[position].isEmpty) {

        node.children[position].begin = begin;
        node.children[position].isEmpty = false;
        node.children[position].end = begin;
      } else if (!node.children[position].hasChildren) {
        string::iterator found = checkRepeat(node.children[position].begin, node.children[position].end, *begin);
        if (found != node.children[position].end && found != end) {
          if (*(found + 1) != *(begin + 1) && (found + 1) != end) {
            cout << *found << " - nashel. " << *node.children[position].end << endl;
            node.children[position].children.reset(new TreeNode[overallLength - edge]);
            node.children[position].children[0].end = node.children[position].end;
            node.children[position].end = found;
            found++;
            node.children[position].children[0].begin = found;
            node.children[position].children[0].isEmpty = false;
            node.children[position].hasChildren = true;
          }
        } else {
          node.children[position].end = begin;
        }
      } else {
        extension(node.children[position], overallLength - edge, begin, end);
      }
    }
  }

  string::iterator checkRepeat(string::iterator begin, string::iterator end, char ch) {
    while (begin < end && *begin != ch) {
      begin++;
    }
    return begin;
  }



  };

#endif //SRC_CPP_SUFFIXTREE_H_
