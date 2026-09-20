# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #How to do BFS with the stack?(Create a queue and add the root to the queue and have a count var for the level, if the queue isnt empty then for the length of the queue pop from the left side of the queue and append whatever was in that popped node and increment the level at the end of the loop)
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while queue:
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            level += 1


        return level
