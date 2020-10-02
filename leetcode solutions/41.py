class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set(nums)
        for i in range(1,1000000000000000000):
            if i not in st:
                return i