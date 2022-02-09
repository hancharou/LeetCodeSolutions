from typing import List


class TwoArraysIterator:
    def __init__(self, arr1: [int], arr2: [int]):
        self.arr1 = arr1
        self.index1 = 0
        self.arr2 = arr2
        self.index2 = 0

        self.sequence_index = 0

        self.median_indexes = []
        total = len(arr1) + len(arr2)
        half = int(total / 2)
        self.median_indexes = [half]
        if total % 2 != 1:
            self.median_indexes.insert(0, half-1)
        self.median_array = []
        self.max_index = self.median_indexes[-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_index < self.sequence_index:
            raise StopIteration

        item1 = self.arr1[self.index1] if self.index1 < len(self.arr1) else None
        item2 = self.arr2[self.index2] if self.index2 < len(self.arr2) else None

        if item1 is not None and item2 is not None:
            if item1 > item2:
                result = item2
                self.index2 += 1
            else:
                result = item1
                self.index1 += 1
        elif item1 is not None:
            result = item1
            self.index1 += 1
        elif item2 is not None:
            result = item2
            self.index2 += 1
        else:
            raise StopIteration

        if self.sequence_index in self.median_indexes:
            self.median_array += [result]

        self.sequence_index += 1
        return result

    def get_median(self):
        if len(self.median_array) == 1:
            return float(self.median_array[0])
        return (self.median_array[0] + self.median_array[1]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        two_iter = TwoArraysIterator(nums1, nums2)
        for a in two_iter:
            pass
        return two_iter.get_median()


if __name__ == '__main__':
    s = Solution()
    r = s.findMedianSortedArrays([], [0])
    print(r)