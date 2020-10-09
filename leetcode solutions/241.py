from collections import defaultdict
class Solution:
    def __init__(self):
        self.ddic = defaultdict(list)
    def diffWaysToCompute(self, input: str) -> List[int]:
        if self.ddic[input]:
            return self.ddic[input]
        elif input.isnumeric():
            return [int(input)]
        else:
            res = []
            for i in range(len(input)):
                if input[i] in "*+-":
                    left_part = self.diffWaysToCompute(input[:i])
                    right_part = self.diffWaysToCompute(input[i+1:])
                    for a in left_part:
                        for b in right_part:
                            if input[i] == "+":
                                res.append(a + b)
                            elif input[i] == "*":
                                res.append(a*b)
                            elif input[i] == "-":
                                res.append(a - b)
            self.ddic[input] = res
            return res
