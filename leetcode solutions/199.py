class Solution:
    res  = []
    def rightSideView(self, root: TreeNode) -> List[int]:
        def right_view(node, height):
          if node is None:
              return 
          elif height == len(self.res):
              self.res.append(node.val)
          right_view(node.right, height+1)
          right_view(node.left, height+1)
        self.res = []
        right_view(root,0)
        return self.res
    
        