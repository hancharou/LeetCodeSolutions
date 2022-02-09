class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def build_hash(line: str):
            hash_map = {}
            for ch in line:
                hash_map[ch] = hash_map.get(ch, 0) + 1
            return hash_map
        h1 = build_hash(s)
        h2 = build_hash(t)
        for ch, num in h1.items():
            h2[ch] = h2[ch]-num
        for ch, num in h2.items():
            if num == 1:
                return str(ch)


def main():
    solution = Solution()
    assert solution.findTheDifference('', 'y') == 'y'
    assert solution.findTheDifference('abcd', 'bcdea') == 'e'


if __name__ == '__main__':
    main()
