# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive DFS
        # if not root:
        #     return 0
        
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

        #iterative BFS
        #[1,2,3,null,null,4]
        #q=[4], depth = 3, pop = 3
        if not root:
            return 0

        depth = 0
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)      
                if popped.right:
                    q.append(popped.right)
            depth += 1

        return depth
        

        #iterative DFS