from typing import List
from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass

class OperatorNode(Node):
    def __init__(self, operator):
        self.operator = operator
        self.left: Node = None
        self.right: Node = None

    def add_left(self, node: Node):
        self.left = node

    def add_right(self, node: Node):
        self.right = node

    def evaluate(self) -> int:
        match self.operator:
            case '-':
                return int(self.left.evaluate() - self.right.evaluate())
            case '+':
                return int(self.left.evaluate() + self.right.evaluate())
            case '*':
                return int(self.left.evaluate() * self.right.evaluate())
            case '/':
                return int(self.left.evaluate() / self.right.evaluate())

class OperandNode(Node):
    def __init__(self, digit):
        self.digit = digit

    def evaluate(self) -> int:
        return self.digit


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> Node:

        def is_operator(op_str):
            return op_str in ['-', '+', '*', '/']

        stack = []
        for item in postfix:
            if is_operator(item):
                node = OperatorNode(item)
                node.add_right(stack[-1])
                stack = stack[0:-1]
                node.add_left(stack[-1])
                stack = stack[0:-1]
                stack.append(node)
            else:
                stack.append(OperandNode(int(item)))

        return stack[0]

if __name__ == '__main__':
    s = ["3", "4", "+", "2", "*", "7", "/"]
    s2 = ["4","5","2","7","+","-","*"]
    obj = TreeBuilder()
    expTree = obj.buildTree(s)
    result = expTree.evaluate()
    print(result)
    expTree = obj.buildTree(s2)
    result = expTree.evaluate()
    print(result)



