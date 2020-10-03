
from math import inf
class Solution:
    temp = -inf
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.trav(root)
        return self.temp
    
    def trav(self,node):
        if node is None:
            return 0
        l = self.trav(node.left)
        r = self.trav(node.right)
        self.temp = max(node.val ,node.val + l + r ,self.temp)
        return max(node.val + max(l,r) , 0)