//
// Created by Emery Reva on 4/10/22.
//

#include "SuffixTree.h"

bool SuffixTree::search(string input, size_t _threshold) {
  threshold = _threshold;
  bool found{false};
  fBegin = input.begin(), fEnd = input.end();
  down(root.children[0]);
  auto size = result.size();
  if (size) {
    found = true;
  }
  for (size_t iteration{}; iteration < size; iteration++) {
    auto res = result.front();
    result.pop_front();
    cout << "sequence of length = " << res.second - res.first + 1
         << " found at haystack offset " << distance(hayStack.begin(), res.first) << " needle offset " << iteration << endl;
  }
  return found;
}

void SuffixTree::down(TreeNode& node) {
  string::iterator findBegin{};
  TreeNode* findNode{};
  bool found = searchStart(node, findBegin, findNode, node.begin);
  if (found) {
    /* Думаю, что если бы линки работали так, как должны, то тут можно было бы посчитать, сколько раз они друг за другом накиданы, и все */
    downTillEnd(*findNode, findBegin, findBegin, fBegin);
  }
  if (fBegin != fEnd) {
    fBegin++;
    if (found && findNode->isLinked) {
      /* Если мы уже нашли подстроку, то, сдвинувшись на одну позицию, мы найдем еще одну
       * (что и происходит). Правильно рабочие линки уводили бы (и уводили, но со скоростью O(N^3))
       * подальше отсюда, чтобы не повторяться */
      down(findNode->link->children[0]);
    }
  }
}

bool SuffixTree::grantAccess(string::iterator findBegin) {
  bool access {true};
  for (auto iter = bannedPositions.begin(); iter < bannedPositions.end(); iter++) {
    if (findBegin >= iter->first && findBegin <= iter->second) {
      access = false;
      break;
    }
  }
  return access;
}

void SuffixTree::downTillEnd(TreeNode& node, string::iterator find, string::iterator findBegin, string::iterator toFind) {
  string::iterator findEnd{findBegin};
  TreeNode* findNode{};
  if (node.hasChildren) {
    /* Возвращаем в диапазон наш итератор поиска, если он, вдруг, выбился */
    if (find > *node.end && find < node.begin) {
      find = node.begin;
    }
    /* Пока все совпадает - все в порядке. Как только нет - начинаем пушащие в лист процессы и брейкаем*/
    while (find <= *node.end && toFind < fEnd) {
      if (*find == *toFind) {
        findEnd = find;
        toFind++;
        find++;
      } else {
        if (distance(findEnd, findBegin) >= threshold && findBegin != fEnd) {
          if (grantAccess(findBegin, findEnd)) {
            result.push_back(make_pair(findBegin, findEnd));
            bannedPositions.push_back(make_pair(findBegin, findEnd));
          }
        }
        findBegin = fEnd;
        toFind = fBegin;
        break;
      }
    }
    /* И если наш итератор, указывающий на начальную позицию искомой подстроки в строке, указывает в
     * условно никуда, то надо его вернуть. И если дальше ничего не нашли - все, хватит.*/
    if (findBegin == fEnd) {
      bool found = searchStart(node, findBegin, findNode, find);
      if (found) {
        find = findBegin;
        downTillEnd(*findNode, find, findBegin, toFind);
      }
    } else {
      downTillEnd(node.children[0], find, findBegin, toFind);
    }
  }
}

bool SuffixTree::searchStart(TreeNode& node, string::iterator& findBegin, TreeNode*& findNode, string::iterator position) {
  bool found{false};
  string::iterator find{position};
  while (find <= *node.end && !found) {
    if (*find == *fBegin) {
      found = true;
      findBegin = find;
      findNode = &node;
    } else {
      find++;
    }
  }
  if (!found && node.hasChildren) {
    found = searchStart(node.children[0], findBegin, findNode, node.children[0].begin);
  }
  return found;
}

void SuffixTree::construct() {
  root.children.reset(new TreeNode[overallLength]);
  root.hasChildren = true;
  string::iterator begin {hayStack.begin()}, end {hayStack.end()};
  size_t edge{};
  for (; begin < end; begin++, edge++) {
    finalEND = begin;
    extension(root, edge, begin, end);
    remainingLength--;
  }
}

void SuffixTree::extension(TreeNode& node, size_t edge, string::iterator& begin, string::iterator& end) {
  bool raised{false};
  for (size_t position = 0; position <= edge; position++) {
    /*  Если здесь пусто, то нужно бы создать нод */
    if (node.children[position].isEmpty) {
      node.children[position].begin = begin;
      node.children[position].isEmpty = false;
      node.children[position].end = &finalEND;
    } else if (!node.children[position].hasChildren) {
      string::iterator found = checkRepeat(node.children[position].begin, *node.children[position].end, *begin);
      if (found != *node.children[position].end && found != end) {
        if (*(found + 1) != *(begin + 1) && (found + 1) != end) {
          constructNewNode(node.children[position], found);
          /*  Собственно создается новый линк, либо готовится к созданию. По правильно построенным линкам можно было бы искать
           * со скоростью света, но я пока что не кибергений( */
          if (needToLink) {
            toLink->link = &node.children[position];
            toLink->isLinked = true;
            toLink = &node.children[position];
          } else {
            needToLink = true;
            toLink = &node.children[position];
          }
          edge--;
        }
      } else if (!raised){
        /*  Хорошая штука, что у всех пацанов, у которых есть способный к движению конец, конец передвигается на один. Экономит время экспоненциально.
         */
        finalEND++;
        raised = true;
//          break;
        /* Если здесь оставить break, то все летает. Но дерево правильно не ветвится, не знаю, как это починить( */
      }
    } else {
      extension(node.children[position], remainingLength, begin, end);
    }
  }
}

string::iterator SuffixTree::checkRepeat(string::iterator begin, string::iterator end, char ch) {
  while (begin <= end && *begin != ch) {
    begin++;
  }
  return begin;
}

void SuffixTree::constructNewNode(TreeNode& node, string::iterator& found) {
  node.children.reset(new TreeNode[remainingLength]);
  node.children[0].end = &finalEND;
  *node.end = found;
  found++;
  node.children[0].begin = found;
  node.children[0].isEmpty = false;
  node.hasChildren = true;
}
