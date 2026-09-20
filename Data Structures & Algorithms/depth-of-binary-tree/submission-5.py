# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #How to do DFS with stack?(Create a stack that has the root and the depth
        #and whil theres items in the stack, pop the item in the stack and if there is a value then calculate the res depth and append the result left and right and add to the depth)
        stack = [[root, 1]]
        res = 0
        while stack:
            popped, depth = stack.pop()
            if popped:
                res = max(res,depth)
                stack.append([popped.left, depth+1])
                stack.append([popped.right, depth+1])
        
        return res



        #How to do BFS with the stack?(Create a queue and add the root to the queue and have a count var for the level, if the queue isnt empty then for the length of the queue pop from the left side of the queue and append whatever was in that popped node and increment the level at the end of the loop)
