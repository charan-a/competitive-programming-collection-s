class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        mergedlst = []
        for i in range(1, len(intervals)):
            ele = intervals[i]
            if ele[0] < end:
                end = max(ele[1],end)
            else:
                mergedlst.append([start,end])
                start = ele[0]
                end = ele[1]
        mergedlst.append([start,end])
        return mergedlst