class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i = 0
        j = l-1
        mx = 0
        while( i < j):
            temp = (j-i)*min(height[i],height[j])
            mx = max(mx,temp)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return mx