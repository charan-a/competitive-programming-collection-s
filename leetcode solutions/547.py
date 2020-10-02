class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    def dfs(i):
      for idx , val in enumerate(M[i]):
        if val == 1 and idx not in seen:
          seen.add(idx)
          dfs(idx)
    
    
    l = len(M)
    seen = set()
    cnt = 0
    for i in range(l):
      if i not in seen:
        dfs(i)
        cnt += 1
    return cnt
  
    

    
      