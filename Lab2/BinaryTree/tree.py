import copy


class Tree:
    SPACE_COUNT = 5

    @staticmethod
    def _rotateright(p):
        q = p.left
        if not q:
            return p
        p.left = q.right
        q.right = p
        return q

    @staticmethod
    def _rotateleft(q):
        p = q.right
        if not p:
            return q
        q.right = p.left
        p.left = q
        return p

    @staticmethod
    def _insertroot(p, k):
        if not p:
            return Tree(k)
        if k <= p.key:
            p.left = Tree._insertroot(p.left, k)
            return Tree._rotateright(p)
        else:
            p.right = Tree._insertroot(p.right, k)
            return Tree._rotateleft(p)

    def __init__(self, key, left=None, right=None):
        if isinstance(key, Tree):
            self.clone(key)
        else:
            self.key = key
            self.left = left
            self.right = right

    def find(self, k):
        if k == self.key:
            return self
        if k < self.key and self.left is not None:
            return self.left.find(k)
        if k > self.key and self.right is not None:
            return self.right.find(k)
        return None

    def insert(self, k):
        if k <= self.key:
            if self.left is None:
                self.left = Tree(k)
            else:
                self.left = self.left.insert(k)
        else:
            if self.right is None:
                self.right = Tree(k)
            else:
                self.right = self.right.insert(k)
        return self

    def insertroot(self, k):
        self.clone(self._insertroot(self, k))

    def remove(self, k):
        x = self
        y = None
        while x is not None:
            if k == x.key:
                break
            else:
                y = x
                if k < x.key:
                    x = x.left
                else:
                    x = x.right

        if x is None:
            return

        if x.right is None:
            if y is None:
                self.clone(x.left)
            else:
                if x == y.left:
                    y.left = x.left
                else:
                    y.right = x.left
        else:
            leftmost = x.right
            y = None
            while leftmost.left is not None:
                y = leftmost
                leftmost = leftmost.left

            if y is not None:
                y.left = leftmost.right
            else:
                x.right = leftmost.right

            x.key = leftmost.key

    def _print_node(self, space):
        space += self.SPACE_COUNT
        if self.right is not None:
            self.right._print_node(space)
        print()
        for i in range(self.SPACE_COUNT, space):
            print(' ', end='')
        print('%d\n' % self.key)
        if self.left is not None:
            self.left._print_node(space)

    def clone(self, to_clone):
        self.__dict__.update(copy.deepcopy(to_clone.__dict__))

    def show(self):
        self._print_node(0)


if __name__ == '__main__':
    t = Tree(5)
    t.insert(3)
    t.insert(7)
    t.insertroot(4)
    t.insertroot(8)
    t.insert(6)
    t.insert(10)
    t.insert(20)
    t.remove(20)
    t.remove(5)
    t.show()
