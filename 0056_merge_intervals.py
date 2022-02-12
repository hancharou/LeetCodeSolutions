from typing import List
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(intervals):
            j = i + 1
            start, end = intervals[i]
            max_index = -1
            while j < len(intervals):
                check_start, check_end = intervals[j]
                if check_start <= end:
                    end = max(check_end, end)
                    max_index = j
                j += 1
            result.append([start, end])
            if max_index > 0:
                i = max_index+1
            else:
                i += 1

        return result


class Stack:

    def __init__(self, first=None):
        self.stack = deque()
        if first:
            self.stack.append(first)

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def push(self, item):
        self.stack.appendleft(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.popleft()

    def list(self):
        return list(self.stack)


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        stack = Stack(intervals[0])
        i = 1
        while i < len(intervals):
            top = stack.peek()
            top_start, top_end = top[0], top[1]
            next_start, next_end = intervals[i][0], intervals[i][1]
            if top_end < next_start:
                stack.push(intervals[i])
            elif top_end < next_end:
                top[1] = intervals[i][1]
                stack.pop()
                stack.push(top)
            i += 1

        return stack.list()


class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            top = result[-1]
            top_start, top_end = top[0], top[1]
            next_start, next_end = intervals[i][0], intervals[i][1]
            if top_end < next_start:
                result.append(intervals[i])
            elif top_end < next_end:
                top[1] = intervals[i][1]
                result = result[0:-1]
                result.append(top)
            i += 1

        return list(result)

if __name__ == '__main__':
    s = Solution3()
    #r = s.merge([[1,4],[0,1]])
    #assert r == [[0,4]]
    # r = s.merge([[1,3],[2,6],[8,10],[15,18]])
    # assert r == [[1,6],[8,10],[15,18]]
    # r = s.merge([[1,4],[4,5]])
    # assert r == [[1,5]]
    # r = s.merge([[1,4],[0,4]])
    # assert r == [[0,4]]
    #
    # r = s.merge([[1, 4], [4,5], [5, 7]])
    # r = s.merge([[1,4],[0,4]])
    # r = s.merge([[2,3],[5,5],[2,2],[3,4],[3,4]])
    r = s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
    print(r)
    assert r == [[1,3],[4,7]]
