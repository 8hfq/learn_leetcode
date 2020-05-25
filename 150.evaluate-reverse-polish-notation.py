#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-',"*","/"]:
                stack.append(tokens[i])
            else:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if tokens[i] =='+':
                        stack.append(num1+num2)
                    if tokens[i] =='-':
                        stack.append(num2-num1)
                    if tokens[i] =='*':
                        stack.append(num1*num2)
                    if tokens[i] =='/':
                        stack.append(num2/num1)
        return int(stack.pop())

        
        
# @lc code=end

