from BinaryTree import BinaryTree

tree = BinaryTree()


def test_insert():
    tree.push(3)
    assert tree.root.value == 3
    tree.push(4)
    assert tree.root.right.value == 4
    tree.push(2)
    assert tree.root.left.value == 2
    tree.push(8)
    assert tree.root.right.right.value == 8
    tree.push(65)
    assert tree.root.right.right.right.value == 65
    tree.push(-4)
    assert tree.root.left.left.value == -4
    tree.push(6)
    assert tree.root.right.right.left.value == 6
    tree.push(1)
    assert tree.root.left.left.right.value == 1


def test_preorder_traversal():
    assert tree.preorder_traversal() == [3, 2, -4, 1, 4, 8, 6, 65]


def test_inorder_traversal():
    assert tree.inorder_traversal(tree.root, []) == [-4, 1, 2, 3, 4, 6, 8, 65]


def test_postorder_traversal():
    assert tree.postorder_traversal(tree.root, []) == [1, -4, 2, 6, 65, 8, 4, 3]
