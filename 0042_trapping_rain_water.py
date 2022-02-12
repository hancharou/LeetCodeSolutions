from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        temp_volume = 0
        prev_h = 0
        open_in_height = 0
        open_in = False
        for i in range(0, len(height)):
            h = height[i]
            if h < prev_h and not open_in:
                open_in = True
                open_in_height = prev_h

            if open_in and open_in_height <= h:
                volume += temp_volume
                open_in = False
                temp_volume += 0

            if open_in:
                temp_volume += open_in_height - h

            prev_h = h
        return volume


if __name__ == '__main__':
    s = Solution()
    v = s.trap([4,2,3])
    print(v)

