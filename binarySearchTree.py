class BSTnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.totalHeight = 0
        self.root = None

    # Inserts a node into a binary search tree
    def insert(self, value):
        # checks if tree is empty
        if self.root is None:
            self.root = BSTnode(value)
            return
        # checks if root is duplicate
        if self.root == value:
            return

        node = self.root
        while True:
            # go to left subtree
            if value < node.value:
                if node.left is None:
                    node.left = BSTnode(value)
                    return
                node = node.left
            # go to right subtree
            else:
                if node.right is None:
                    node.right = BSTnode(value)
                    return
                node = node.right

    def inOrderDisplay(self):
        result = []
        self.inOrder(self.root, result)
        return result

    # In order traversal display to help visualize the tree
    def inOrder(self, node, result):
        if node is not None:
            self.inOrder(node.left, result)
            result.append(node.value)
            self.inOrder(node.right, result)

    # In Order Traversal to help with retrieving total height of all nodes
    def totalHeightTraversal(self, node, height):
        if node is not None:
            self.totalHeightTraversal(node.left, height + 1)
            self.totalHeight += height
            self.totalHeightTraversal(node.right, height + 1)

    # computes the sum of the heights of all nodes in tree
    def getTotalHeight(self):
        self.totalHeightTraversal(self.root, 0)
        return self.totalHeight

    # delete one node in BST recursively
    def delete(self, value):
        self.root = self.deleteRecursive(self.root, value)

    def deleteRecursive(self, node, value):
        # Base case
        if node is None:
            return None

        # Searching for node to delete
        if value < node.value:
            node.left = self.deleteRecursive(node.left, value)
            return node
        elif value > node.value:
            node.right = self.deleteRecursive(node.right, value)
            return node

        else:
            # Case 1 : node has no children
            if node.left is None and node.right is None:
                return None

            # Case 2 : node has only one child so attach the
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3 : node has 2 children
            else:
                minimum = node.right
                while minimum.left is not None:
                    minimum = minimum.left
                node.value = minimum.value
                node.right = self.deleteRecursive(node.right, minimum.value)
                return node

    # Saves a binary tree into a string representation
    def save(self):
        result = []
        self.inOrder(self.root, result)
        return ','.join(str(i) for i in result)

    # Restores a string representation of a tree in order,
    def restore(self, inputString):
        values = [int(i) for i in inputString.split(',')]
        for val in values:
            self.insert(val)


def main():
    nums = [5, 3, 7, 2, 4, 6, 8]
    bst = BinarySearchTree()
    print("before insertion: ")
    print(bst.inOrderDisplay())
    for num in nums:
        bst.insert(num)

    print("After inserting and before deletion:")
    print(bst.inOrderDisplay())
    newSumOfHeights = bst.getTotalHeight()
    print("sum of heights: " + str(newSumOfHeights))

    bst.delete(3)

    print("After deletion:")
    print(bst.inOrderDisplay())

    bst_string = bst.save()
    print("Saved BST string: "+ bst_string)
    newBst = BinarySearchTree()
    newBst.restore(bst_string)
    print("Restored Tree Inorder: ")
    # save the details in bst and they are restored into newBst
    print(newBst.inOrderDisplay())

if __name__ == '__main__':
    main()
