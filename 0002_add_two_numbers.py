from typing import Optional
from itertools import zip_longest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current:
            result = self.current.val
            self.current = self.current.next
        else:
            raise StopIteration
        return result


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        over = 0
        for i1, i2 in zip_longest(l1, l2):
            if i1:
                over += i1
            if i2:
                over += i2
            result.append(over % 10)
            over = 0 if over < 10 else 1
        if over > 0:
            result.append(over)
        root = None
        for num in reversed(result):
            node = ListNode(num, root)
            root = node
        return root


if __name__ == '__main__':
    solution = Solution()
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    r = solution.addTwoNumbers(l1, l2)
    for i in r:
        print(i)
