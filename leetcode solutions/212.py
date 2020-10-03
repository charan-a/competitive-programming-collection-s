class trie():    
    def __init__(self):
        self.children = {}
        
    def insert(self,word):
        curr = self.children
        for c in word:
            curr = curr.setdefault(c,{})
        curr["$"] = True
    def search(self,word):
        curr = self.children
        for c in word:
            curr = curr.get(c)
            if not curr :
                return False
        return "$" in curr and curr["$"]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        Trie = trie()
        node = Trie.children
        n = len(board)
        m = len(board[0])
        path = ""
        for word in words:
            Trie.insert(word)
        for i in range(n):
          for j in range(m):
            self.dfs(board,node ,i,j,path,res)
        return res
        
        
    def dfs(self,board,node,i,j,path,res):
        if "$" in node and node["$"]:
            res.append(path)
            node["$"] = False
          
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
      
        ch = board[i][j]
        if ch in node:
            board[i][j] = "#"
            self.dfs(board,node[ch],i+1,j,path+ch,res)
            self.dfs(board,node[ch],i,j+1,path+ch,res)
            self.dfs(board,node[ch],i-1,j,path+ch,res)
            self.dfs(board,node[ch],i,j-1,path+ch,res)
            board[i][j] = ch
        else:
            return