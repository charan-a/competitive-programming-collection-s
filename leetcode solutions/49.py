from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            ddict[tuple(cnt)].append(s)
        return ddict.values()