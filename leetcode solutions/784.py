class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        lst = []
        l = len(S)
        lst.append(S)
        for i in range(l):
            char = S[i]
            if 64 < ord(char) < 91 or 96 < ord(char) < 123 :
                limit = len(lst)
                new_lst = []
                for j in range(limit):
                    sg = lst[j]
                    temp = sg[:i] + char.upper() + sg[i+1:]
                    new_lst.append(temp)
                    temp = sg[:i] + char.lower() + sg[i+1:]
                    new_lst.append(temp)
                lst = new_lst
        return lst
