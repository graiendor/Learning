//
// Created by Emery Reva on 4/14/22.
//

#include "ExponentialSearch.h"

list needleSearch(string& haystack, string needle, size_t threshold) {
  list result{};
  vector bannedPositions{};
  string::iterator begin = haystack.begin(), end = haystack.end(), toFind = needle.begin(), edge = haystack.begin();
  while (toFind != needle.end()) {
    string::iterator findBegin{}, findEnd{};
    size_t binary = 2;
    edge = haystack.begin();
    while (edge <= end) {
      findBegin = std::find(begin, edge, *toFind);
      findEnd = findBegin;
      if (findBegin != edge) {
        followRepeat(findBegin, end, toFind, findEnd);
        if (std::distance(findBegin, findEnd) >= threshold - 1 && grantAccess(findBegin, bannedPositions)) {
          result.push_back(std::make_pair(findBegin, findEnd));
          bannedPositions.push_back(std::make_pair(findBegin, findEnd));
        }
      }
      begin = edge;
      if (findEnd > edge) {
        begin = findEnd;
      }
      pow(binary, 2);
      if (edge + binary < end) {
        std::advance(edge, binary);
      } else if (edge == end) {
        break;
      } else {
        edge = end;
      }
    }
    toFind++;
  }
  return result;
}

bool grantAccess(string::iterator findBegin, vector& bannedPositions) {
  bool access {true};
  for (auto iter = bannedPositions.begin(); iter < bannedPositions.end(); iter++) {
    if (findBegin >= iter->first && findBegin <= iter->second) {
      access = false;
      break;
    }
  }
  return access;
}

void followRepeat(string::iterator findBegin, const string::iterator& end, string::iterator toFind, string::iterator& findEnd) {
  bool found{true};
  toFind++;
  findBegin++;
  while (findBegin <= end && found) {
    if (*findBegin != *toFind) {
      found = false;
      findBegin--;
      findEnd = findBegin;
    } else {
      findBegin++;
      toFind++;
    }
  }
}
