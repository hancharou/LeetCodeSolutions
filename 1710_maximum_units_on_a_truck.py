from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        index = 0
        while truckSize > 0 and index < len(boxTypes):
            take = truckSize - boxTypes[index][0]
            if take > 0:
                result += boxTypes[index][0] * boxTypes[index][1]
                truckSize -= boxTypes[index][0]
            else:
                result += truckSize * boxTypes[index][1]
                truckSize -= truckSize
            index += 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maximumUnits([[1,3],[2,2],[3,1]], 4)
    print(r)
    r = s.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35)
    print(r)