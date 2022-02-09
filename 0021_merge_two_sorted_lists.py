from typing import List
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeIterator:
    def __init__(self, node1: ListNode, node2: ListNode):
        self.list1 = node1
        self.list2 = node2

    def __iter__(self):
        return self

    def __next__(self):
        item1 = self.list1.val if self.list1 else None
        item2 = self.list2.val if self.list2 else None

        if item1 is not None and item2 is not None:
            if item1 > item2:
                result = item2
                self.list2 = self.list2.next
            else:
                result = item1
                self.list1 = self.list1.next
        elif item1 is not None:
            result = item1
            self.list1 = self.list1.next
        elif item2 is not None:
            result = item2
            self.list2 = self.list2.next
        else:
            raise StopIteration
        return result

class Solution:
    def mergeTwoLists(self, l1, l2):
        s = deque()
        for i in ListNodeIterator(l1, l2):
            s.append(i)
        root = None
        while len(s):
            root = ListNode(s.pop(), root)
        return root

if __name__ == '__main__':
    def build_nodes(l: [int]) -> ListNode:
        root = None
        for i in reversed(l):
            root = ListNode(i, root)
        return root
    l1 = build_nodes([1, 2, 4])
    l2 = build_nodes([1, 3, 4])

    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    #for r in ListNodeIterator(result):
    #    print(r)
