class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        curr_end = 0
        curr_far = 0
        jumps = 0
        
        for i in range(l-1):
            curr_far = max(curr_far,i + nums[i])
            
            if i == curr_end:
                jumps += 1
                curr_end = curr_far
        return jumps 
        