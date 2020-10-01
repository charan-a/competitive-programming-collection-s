from collections import Counter, defaultdict
import string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_l = len(p)
        s_l = len(s)
        idxs = []
        if s_l < p_l:
            return idxs
        pval = 0
        sval = 0
        for i in range(p_l):
            pval += hash(p[i])
            sval += hash(s[i])
        if pval == sval:
            idxs.append(0)
        for i in range(p_l,s_l):
            sval += hash(s[i])
            sval -= hash(s[i - p_l])
            if pval == sval:
                idxs.append(i - p_l + 1)

        return idxs
        