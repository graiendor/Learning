//
// Created by Emery Reva on 4/14/22.
//

#ifndef SRC_CPP_SUFFIXTREE_H_
#define SRC_CPP_SUFFIXTREE_H_
#include <string>
#include <memory>
#include <list>
#include <vector>
#include <iostream>
#include <chrono>

using namespace std;

class SuffixTree {
 private:
  string hayStack{};
  size_t overallLength{};
  size_t remainingLength{};
  bool needToLink {false};
  list<std::pair<string::iterator, string::iterator>> result{};
  size_t threshold{};
  string::iterator fBegin{};
  string::iterator fEnd{};

  string::iterator finalEND{};

  struct TreeNode {
    shared_ptr<TreeNode[]> children{};  // люблю-обожаю умные указатели
    TreeNode* link{};                   // люблю, но не обожаю сырые указатели
    string::iterator begin{};
    string::iterator* end{};
    bool isEmpty{true};
    bool isLinked{false};
    bool hasChildren{false};
  };

  TreeNode root{};
  TreeNode* toLink{};

  vector<std::pair<string::iterator, string::iterator>> bannedPositions{};

  /* Чтобы найти самое сокровенное, нужно спуститься в самые далекие глубины. Спускаемся по древу,
   * пока не найдем все вхождения. Двигаем начало искомой подстроки и спускаемся дальше */
  void down(TreeNode& node);


  /* Костыль года. Пускаем в наш лист найденных вхождений только вхождения, не входящие в уже найденные.  */
  bool grantAccess(string::iterator findBegin);

  /* Спускаемся до самого конца. Пока у этой ветви есть дети (а это самое глубокое, нулевое, подземелье) ищем пару -
   * начало и конец вхождения. Как только находим - сразу пушим (если наш костыль года пропускает) */
  void downTillEnd(TreeNode& node, string::iterator find, string::iterator findBegin, string::iterator toFind);

  /* Ищем то место (итератор) и тот нод, где у нас есть совпадение с искомым символом. Сохраняем их
   * ведь там начнется продолжение этого поиска. */
  bool searchStart(TreeNode& node, string::iterator& findBegin, TreeNode*& findNode, string::iterator position);


  void construct();

  /* Собственно расширение дерева по трем правилам:
   * 1. Если пусто, заполняем.
   * 2. Если не пусто и посередине начинается несостыковка, то разделяем и властвуем.
   * 3. Если не пусто, но уже все есть, то ничего не нужно.*/
  void extension(TreeNode& node, size_t edge, string::iterator& begin, string::iterator& end);

  string::iterator checkRepeat(string::iterator begin, string::iterator end, char ch);

  /*  Создает новый нод, разделяя предыдущий на два - до и после.
   * Нужно поставить конец родителя место до разрыва, создать в новом ноде
   * хвост от родителя и создать в новом ноде новый путь  */
  void constructNewNode(TreeNode& node, string::iterator& found);

 public:
  SuffixTree(string input) : hayStack(input) {
    overallLength = hayStack.length();
    remainingLength = overallLength;
    construct();
  }

  /* Нужно подать подстроку, которую необходимо найти и длинна которая равна или превышает threshold.
   * Возвращает true, если хоть что-то нашлось. */
  bool search(string input, size_t _threshold);

  };

#endif //SRC_CPP_SUFFIXTREE_H_
