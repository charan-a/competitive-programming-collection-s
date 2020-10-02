from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ctr = Counter(tasks)
        vals = list(ctr.values())
        taskslength = sum(vals)
        mx = max(vals)
        noofmx = vals.count(mx)
        freespace = (mx-1)*(n - (noofmx - 1))
        idles = max(0, freespace - (taskslength - noofmx * mx))
        return taskslength + idles