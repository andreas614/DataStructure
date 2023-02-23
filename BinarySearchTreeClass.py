# Binary Search Tree Class

class BST:
    class _Node:
        def __init__(self, val, left = None, right = None):
            self._value = val
            self._left = left
            self._right = right

    def __init__(self, root = None):
        self._root = root

    def __str__(self):
        return self._str_helper(self._root)

    def _str_helper(self, root):
        if not root:
            return ''
        left = self._str_helper(root._left)
        right = self._str_helper(root._right)
        ret = str(root._value)
        if left:
            ret = left + ' ' + ret
        if right:
            ret = ret + ' ' + right
        return ret

    def print_pretty(self):
        self._print_pretty_helper(self._root, 0)

    def _print_pretty_helper(self, root, depth):
        if not root:
            return
        self._print_pretty_helper(root._right, depth + 1)
        print('\t'*depth, root._value)
        self._print_pretty_helper(root._left, depth + 1)

    def insert(self, val):
        if not self._root:
            self._root = BST._Node(val)
        else:
            self._insert_helper(self._root, val)

    def _insert_helper(self, root, val):
        if not root:
            return BST._Node(val)
        else:
            if root._value < val:
                root._right = self._insert_helper(root._right, val)
            else:
                root._left = self._insert_helper(root._left, val)
            return root

    def insert_arr(self, arr):
        if not arr:
            return
        else:
            for val in arr:
                self.insert(val)