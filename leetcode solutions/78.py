class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        coll = [[]]
        for e in nums:
            temp = []
            for lst in coll:
                temp.append(lst)
                temp.append( lst + [e])
            coll = temp
        return coll