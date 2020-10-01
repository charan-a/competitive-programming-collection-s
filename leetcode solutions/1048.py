class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        words.sort(key = len)
        for word in words:
            lst = []
            for i in range(len(word)):
                lst.append(dic.get(word[:i] + word[i+1:] , 0) + 1)
            dic[word] = max(lst)
        return max(dic.values())