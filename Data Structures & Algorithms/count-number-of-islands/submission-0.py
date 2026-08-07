class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        #         Input: grid = [
        #     ["1","1","0","0","1"],
        #     ["1","1","0","0","1"],
        #     ["0","0","1","0","0"],
        #     ["0","0","0","1","1"]
        #   ]
        # Output: 4

        #iterate through each element of the grid,
        #when there is a "1", then run bfs and increase the number of islands by one


        numOfIslands = 0
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(i, j):
            q = deque()
            grid[i][j] = "0"
            q.append((i,j))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]=="0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    numOfIslands += 1
                    bfs(i, j)

        return numOfIslands


