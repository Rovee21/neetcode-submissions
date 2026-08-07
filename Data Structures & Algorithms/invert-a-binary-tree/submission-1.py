# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #use recursion to go through the nodes and swap children
        #root = [1,3,2,5,4,6,7]
        #root = [1,3,2,7,6,4,5]

        if not root:
            return None
        
        #swap children:
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        return root