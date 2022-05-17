#include "BinaryTree.h"

int main () {
    BinaryTree tree {};

    auto get = tree.push(3);
    BinaryTree::Iterator iter{get.first};

    get = tree.push(2);
    iter = get.first;

    get = tree.push(4);
    iter = get.first;

    get = tree.push(8);
    iter = get.first;

    tree.clear();
};