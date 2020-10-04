class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def solve(sg,digits):
            if len(digits) == 0:
                lst.append(sg)
            else:
                for i in phone[digits[0]]:
                    solve(sg + i , digits[1:])
        lst = []
        if digits:
            solve('',digits)
        return lst