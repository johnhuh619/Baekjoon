# 트리 만들기
# 전위 순회하기
# 후위 순회하기
# 만든거 배열에 삽입해서 출력하기

import sys
sys.setrecursionlimit(15000)
class Node():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None

def make_tree(nodeinfo):
    nodes = [(x, y, idx+1) for idx, (x,y) in enumerate(nodeinfo)]
    nodes.sort(key = lambda x: (-x[1], x[0]))
    root = Node(nodes[0][0], nodes[0][1], nodes[0][2])
        
    def insert(p, x, y, num):
        # y 좌표가 부모보다 큰가?
        if x < p.x:
            if p.left is None:
                p.left = Node(x, y, num)
            else:
                insert(p.left, x, y, num)
        else:
            if p.right is None:
                p.right = Node(x, y, num)
            else:
                insert(p.right, x, y, num)
    for x, y, num in nodes[1:]:
        insert(root, x, y, num)
    
    return root

def preOrder(node, result):
    if node is None:
        return
    
    result.append(node.num)
    preOrder(node.left, result)
    preOrder(node.right, result)
    
def postOrder(node, result):
    if node is None:
        return
    
    postOrder(node.left, result)
    postOrder(node.right, result)
    result.append(node.num)

def solution(nodeinfo):
    root = make_tree(nodeinfo)
    
    pre = []
    post = []
    preOrder(root, pre)
    postOrder(root, post)

    return [pre, post]