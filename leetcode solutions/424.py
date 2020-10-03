from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ddic = defaultdict(int)
        l = len(s)
        most_freq = 0
        start = 0
        for end in range(l):
            ddic[s[end]] += 1
            most_freq = max( most_freq,  ddic[s[end]])
            if (end - start + 1 - most_freq ) > k :
                ddic[s[start]] -= 1
                start += 1
        return min(most_freq + k , l)
        