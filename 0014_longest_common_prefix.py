from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        search = ''
        if len(strs) > 1:
            for ch in strs[0]:
                new_search = search + ch
                print(new_search)
                if len(list(filter(lambda x: x.startswith(new_search), strs))) < len(strs):
                    return search
                search += ch
            return search
        else:
            return strs[0]



if __name__ == '__main__':
    solution = Solution()
    #assert solution.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    #assert solution.longestCommonPrefix(['dog', 'racecar',  'car']) == ''
    #assert solution.longestCommonPrefix(['']) == ''
    #assert solution.longestCommonPrefix(['a']) == 'a'
    #assert solution.longestCommonPrefix(['hello']) == 'hello'
    assert solution.longestCommonPrefix(['flower', 'flower', 'flower']) == 'flower'
