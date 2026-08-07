class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       #[30,38,30,36,35,40,28]
       #resArr = [1, 4, 1, 2, 1,0,0], stack = [[40,5]]
       resArr = [0] * len(temperatures)
       stack = []
       for i, t in enumerate(temperatures):
        while(stack and stack[-1][0]<t):
            resArr[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append([t,i])

       return resArr