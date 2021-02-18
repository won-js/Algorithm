import sys

input = sys.stdin.readline


class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


def preorder(node):
    print(node.item, end="")
    if node.lchild != ".":
        preorder(tree[node.lchild])
    if node.rchild != ".":
        preorder(tree[node.rchild])


def inorder(node):
    if node.lchild != ".":
        inorder(tree[node.lchild])
    print(node.item, end="")
    if node.rchild != ".":
        inorder(tree[node.rchild])


def postorder(node):
    if node.lchild != ".":
        postorder(tree[node.lchild])
    if node.rchild != ".":
        postorder(tree[node.rchild])
    print(node.item, end="")


n = int(input().rstrip())
tree = {}
for _ in range(n):
    data = input().rstrip().split(" ")
    tree[data[0]] = Node(data[0], data[1], data[2])

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])