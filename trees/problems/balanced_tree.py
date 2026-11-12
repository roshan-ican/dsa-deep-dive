from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right

    def search(self, value):
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def search_recursively(self, value):
        def helper(node):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return helper(node.left)
            else:
                return helper(node.right)

        return helper(self.root)

    def postorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            visit(node.right)
            result.append(node.value)

        visit(self.root)
        return result

    def preorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            result.append(node.value)
            visit(node.left)
            visit(node.right)

        visit(self.root)
        return result

    def inorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self.root)
        return result

    def bfs(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def bfs_levels(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result

    def height(self):
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            return 1 + max(left, right)

        return helper(self.root)

    def find_min(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def find_max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.value

    def delete(self, value):
        def helper(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = helper(node.left, value)
            elif value > node.value:
                node.right = helper(node.right, value)
            else:
                if node.left is None and node.right is None:
                    return None  # case 1: leaf, remove it
                if node.left is None:
                    return node.right  # case 2: only right child
                if node.right is None:
                    return node.left
            return node

        self.root = helper(self.root, value)


t = BST()
for v in [8, 3, 10, 1, 6, 14]:
    t.insert(v)
print(t.inorder())

print(t.search(6))  # True
print(t.search(14))  # True
print(t.search(7))  # False
print(t.search_recursively(1))  # False

print(t.preorder())  # [8, 3, 1, 6, 10, 14]
print(t.postorder())  # [1, 6, 3, 14, 10, 8]
print(t.bfs())  # [8, 3, 10, 1, 6, 14]
print(t.bfs_levels())  # [[8], [3, 10], [1, 6, 14]]
print(t.height())  # 3
print(t.find_min())  # 1
print(t.find_max())  # 14
t.delete(1)
t.delete(10)
print(t.inorder())  # [3, 6, 8, 14]