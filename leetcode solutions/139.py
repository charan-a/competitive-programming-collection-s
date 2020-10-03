class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        arr = [False for i in range(l)]
        for i in range(l):
            for word in wordDict:
                if word == s[i - len(word) + 1 : i + 1] and (arr[i - len(word)] or i - len(word) == -1):
                    arr[i] = True
                    
        return arr[-1]