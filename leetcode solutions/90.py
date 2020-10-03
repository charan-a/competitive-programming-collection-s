class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        start = 0
        end = 0
        nums.sort()
        l = len(nums)
        for i in range(l):
            start = 0
            if i > 0 and nums[i] == nums[i-1]:
                start = end 
            end = len(ans)
            for j in range(start,end):
                sublst = list(ans[j])
                sublst.append(nums[i])
                ans.append(sublst)
        return ans