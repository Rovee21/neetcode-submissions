# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # q=[2,3], popped = 2
        q = deque()
        if root:
            q.append(root)
        
        while q:
            popped = q.popleft()
            temp = popped.right
            popped.right = popped.left
            popped.left = temp
            if popped.right:
                q.append(popped.right)
            if popped.left:
                q.append(popped.left)
        
        return root



