# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS using a queue and an array to track visited nodes
        # root = [1,2,3,4,5,6,7]
        # queue[4,5,6,7], visited = [[1],[2, 3]], level = 1, tempArr = [2, 3]
        visited = []
        if not root:
            return visited
        queue = deque()
        queue.append(root)
        while queue:
            tempArr = []
            for i in range(len(queue)):
                pop = queue.popleft()
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                tempArr.append(pop.val)
            visited.append(tempArr)


        return visited