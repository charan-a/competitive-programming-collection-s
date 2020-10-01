class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 0:
            return False
        for i,val in enumerate(nums):
            j = i
            while nums[j] < 1001:
                if nums[j]*val < 0 :
                    break
                next = (j + nums[j])%l
                if j == next:
                    break
                nums[j] = 1001 + i
                j = next
            if 1001 + i == nums[j]:
                return True
        return False
    