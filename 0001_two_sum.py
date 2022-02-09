from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int):
        tup = list(zip(nums, range(0, len(nums))))
        tup.sort(key=lambda x: x[0])
        for i in range(0, len(tup)):
            tup2 = list(filter(lambda x: x[0] <= target - tup[i][0], tup))
            for j in range(i + 1, len(tup2)):
                if tup[i][0] + tup2[j][0] == target:
                    return [tup[i][1], tup2[j][1]]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for num0 in nums:
            t = target - num0
            i += 1
            for num1 in filter(lambda x: x<=t, nums[i:]):
                if num0 + num1 == target:
                    index0 = nums.index(num0)
                    index1 = nums.index(num1, index0)
                    return [index0, index1]


class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2_map = {}
        i = 0
        while i < len(nums):
            num2_map[nums[i]] = num2_map.get(nums[i], []) + [i]
            i += 1
        i = 0
        for num0 in nums:
            t = target - num0
            if t in num2_map:
                t_indexes = num2_map[t]
                if i in t_indexes and len(t_indexes) > 1:
                    t_indexes.remove(i)
                    return [i, t_indexes[0]]
                elif i not in t_indexes:
                    return [i, t_indexes[0]]
            i += 1

if __name__ == '__main__':
    solution = Solution4()
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
