from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums_hash = {}
        i = 0
        while i < len(nums):
            nums_hash[nums[i]] = nums_hash.get(nums[i], []) + [i]
            i += 1
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                target = -(nums[i] + nums[j])
                if target in nums_hash:
                    for target_index in nums_hash[target]:
                        if i != target_index and j != target_index:
                            result.add((nums[i], nums[j], target))
                j += 1
            i += 1
        return map(list, result)

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        i = 0
        while i < len(nums):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                sum_two = nums[j] + nums[k]
                if sum_two < target:
                    j += 1
                elif sum_two > target:
                    k -= 1
                else:
                    #r.add((nums[i], nums[j], nums[k]))
                    r.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
            i += 1
        return map(list, r)


if __name__ == '__main__':
    s = Solution()
    #result = s.threeSum([-1,0,1,2,-1,-4])
    #result = s.threeSum([-0, 0, 0, 0])
    result = s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    print(list(result))