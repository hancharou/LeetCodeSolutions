class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        i = 0
        l = int(len(s) / 2)
        while i < l:
            if s[i] != s[len(s)-i-1]:
                return False
            i += 1

        return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        l = int(len(s) / 2)
        return s[0:l] == s[len(s)-l:][::-1]


if __name__ == '__main__':
    s = Solution2()
    #assert s.isPalindrome(99) == True
    print(s.isPalindrome(114))
    print(s.isPalindrome(121))
    print(s.isPalindrome(22))
    print(s.isPalindrome(0))
