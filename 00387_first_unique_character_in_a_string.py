from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        index = 0
        while index < len(s):
            if hashmap[s[index]] == 1:
                return index
            index += 1
        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for ch, num in counter.items():
            if num == 1:
                return s.index(ch)
        return -1


if __name__ == '__main__':
    s = Solution2()
    u = s.firstUniqChar("dddccdbba")
    print(u)
