class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = ''
        while i < len(s):
            test_word = s[i]
            j = i + 1
            while j < len(s) and s[j] not in test_word:
                test_word += s[j]
                j += 1
            if len(test_word) > len(longest):
                longest = test_word
            i += 1
        return len(longest)


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = ''
        for i, c in enumerate(s):
            test_word = c
            j = i + 1
            while j < len(s) and s[j] not in test_word:
                test_word += s[j]
                j += 1
            if len(test_word) > len(longest):
                longest = test_word
            i += 1
        return len(longest)


if __name__ == '__main__':
    s = Solution2()
    r = s.lengthOfLongestSubstring('pwwkew')
    print(r)
