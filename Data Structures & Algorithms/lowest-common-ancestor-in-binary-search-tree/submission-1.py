# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

        curr = root
        while curr:
            if curr.val>p.val and curr.val>q.val:
                curr = curr.left
            elif curr.val<p.val and curr.val<q.val:
                curr = curr.right
            else:
                return curr