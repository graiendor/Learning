//
// Created by Emery Reva on 4/14/22.
//

#ifndef SRC_CPP_EXPONENTIALSEARCH_H_
#define SRC_CPP_EXPONENTIALSEARCH_H_

#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <list>
#include <vector>

using typename std::string;
using typename std::cout;
using typename std::endl;

typedef std::list<std::pair<string::iterator, string::iterator>> list;
typedef std::vector<std::pair<string::iterator, string::iterator>> vector;

/* Проверяет, все ли еще в строке последовательно встречается символы из искомой подстроки */
void followRepeat(string::iterator findBegin, const string::iterator& end, string::iterator toFind, string::iterator& findEnd);

/* Находит все вхождения переданной подстроки, длинна которой не меньше, чем threshold */
list needleSearch(string& haystack, string needle, size_t threshold);

/* Проверяет, находится ли найденное вхождение в уже найденных */
bool grantAccess(string::iterator findBegin, vector& bannedPositions);



#endif //SRC_CPP_EXPONENTIALSEARCH_H_
