class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stk = []
        for i in asteroids:
            if i > 0:
                stk.append(i)
            else:
                temp = [i]
                if stk and stk[-1] > 0:
                    while stk and stk[-1] > 0:
                        if stk[-1] < abs(i):
                            stk.pop()
                        elif stk[-1] == abs(i):
                            stk.pop()
                            temp = []
                            break
                        else:
                            temp = []
                            break
                    stk.extend(temp)
                        
                else:
                    stk.append(i)
                    
        return stk
                    