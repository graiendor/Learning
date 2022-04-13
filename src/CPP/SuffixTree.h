//
// Created by Emery Reva on 4/10/22.
//

#ifndef SRC_CPP_SUFFIXTREE_H_
#define SRC_CPP_SUFFIXTREE_H_
#include <string>
#include <memory>
#include <iostream>
#include <list>

#define MAX_CHAR 256

using namespace std;

class SuffixTree {
 public:
  SuffixTree(string input) {
    hayStack = input;
    overallLength = hayStack.length();
    remainingLength = overallLength;
    construct();
  }

  bool search(string input, size_t threshold) {
    bool found{false};
    needle = input;
    string::iterator begin {input.begin()}, end{input.end()}, find{hayStack.begin()};
    size_t iteration{};
    bool cont {true};
//    while (iteration < threshold) {
      downTheTree(root.children[0], begin, end, threshold);
      auto size = result.size();
      if (size) {
        found = true;
      }
      for (int iteration{}; iteration < size; iteration++) {
        auto res = result.front();
        result.pop_front();
        cout << "sequence of length = " << res.second - res.first + 1
             << " found at haystack offset " << distance(hayStack.begin(), res.first) << " needle offset " << iteration << endl;
        for (int i = 0; i < 5; i++) {
          res.second++;
          cout << *res.second;
        }
        cout  << endl;
      }

    return found;
  }

 private:
  string hayStack{};
  string needle{};
  size_t overallLength{};
  size_t remainingLength{};
  bool needToLink {false};
  list<std::pair<string::iterator, string::iterator>> result;
  size_t position = 1;


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
  TreeNode* lastNode{};

  void downTheTree (TreeNode& node, string::iterator begin, string::iterator end, size_t& threshold) {
    bool found{false};
    string::iterator find{node.begin}, findBegin{}, findEnd{};
    string::iterator originBegin = begin;
    std::pair<string::iterator, string::iterator> pairFound{};
    while (find <= node.end && !found) {
      if (*find == *begin) {
        found = true;
        findBegin = find;
        findEnd = find;
      } else {
        find++;
      }
    }
    if (found) {
      searchEnd(node, begin, end, findEnd, find);
      pairFound = make_pair(findBegin, findEnd);
      result.push_back(pairFound);
      threshold--;
      if (threshold != 0) {
        originBegin++;
        downTheTree(*node.children[position].link, originBegin, end, threshold);
        position++;
      }
    }
    if (node.hasChildren && !found) {
      downTheTree(node.children[0], begin, end, threshold);
    }
  }

  void searchEnd(const TreeNode& node, string::iterator& begin, string::iterator& end, string::iterator& findEnd, string::iterator find) {
    bool found{true};
    if (find > node.end && find < end) {
      find = node.begin;
    }
    while (find <= node.end && found && begin < end) {
      if (*begin == *find) {
        begin++;
        findEnd = find;
        find++;
      } else {
        found = false;
      }
    }
    if (found && node.hasChildren && begin < end) {
      searchEnd(node.children[0], begin, end, findEnd, node.children[0].begin);
    }
  }

  void construct() {
    root.children.reset(new TreeNode[overallLength]);
    root.hasChildren = true;
    string::iterator begin {hayStack.begin()}, end {hayStack.end()};
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
          } else {
            break;
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
