class BinaryTree:

    def __init__(self):
        self.root = self.TreeNode()

    class TreeNode:
        def __init__(self, value=None, left=None, right=None, empty = True):
            self.value = value
            self.left = left
            self.right = right
            self.empty = empty
            self.previous = None

    def preorder_traversal(self) -> list[int]:
        """"""
        node = self.root
        checked = []
        traversal = []
        not_totally_checked = True
        if not node.empty:
            traversal.append(node.value)
            checked.append(node)
        while not_totally_checked:
            if not node.left.empty and node.left not in checked:
                node = node.left
                traversal.append(node.value)
                checked.append(node)
            elif not node.right.empty and node.right not in checked:
                node = node.right
                traversal.append(node.value)
                checked.append(node)
            elif node.previous:
                node = node.previous
            else:
                not_totally_checked = False
        checked.clear()
        return traversal

    def inorder_traversal(self, start, traversal):
        # node = self.root
        # checked = []
        # traversal = []
        # not_totally_checked: bool = True
        # if not node.empty:
        #     while not_totally_checked:
        #         if not node.left.empty and node.left not in checked:
        #             node = node.left
        #         elif not node.right.empty and node.right not in checked:
        #             if node not in checked:
        #                 traversal.append(node.value)
        #                 checked.append(node)
        #             node = node.right
        #             traversal.append(node.value)
        #             checked.append(node)
        #         elif node.previous:
        #             if node not in checked:
        #                 traversal.append(node.value)
        #                 checked.append(node)
        #             node = node.previous
        #         else:
        #             not_totally_checked = False
        if not start.empty:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if not start.empty:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def push(self, value):
        node = self.__find_node_to_insert__(value)
        is_inserted = self.__insert__(value, node)
        return is_inserted

    def __insert__(self, value, node: TreeNode):
        is_inserted: bool = False
        if node.empty:
            self.__create_node__(value, node)
            is_inserted = True
        if value < node.value:
            node.left = self.TreeNode()
            node.left.previous = node
            self.__create_node__(value, node.left)
            is_inserted = True
        if value > node.value:
            node.right = self.TreeNode()
            node.right.previous = node
            self.__create_node__(value, node.right)
            is_inserted = True
        return is_inserted

    def __create_node__(self, value, node: TreeNode):
        node.value = value
        node.empty = False
        node.left = self.TreeNode()
        node.right = self.TreeNode()

    def __find_node_to_insert__(self, value):
        node = self.root
        found: bool = False
        while not node.empty and not found:
            if value < node.value:
                if node.left.empty:
                    found = True
                else:
                    node = node.left
            if value > node.value:
                if node.right.empty:
                    found = True
                else:
                    node = node.right
        return node




#
# print(tree.preorder_traversal(tree.root, []))
# print(tree.inorder_traversal(tree.root, []))
# print(tree.postorder_traversal(tree.root, []))


# def test_preorder():


# if __name__ == "__main__":
#     tree = BinaryTree()
#     print(tree.preorder_traversal(tree.root, []))