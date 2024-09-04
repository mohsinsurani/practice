from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visit.add(r,c)
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0,1], [0, -1]]

                for dr, dc in directions:
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(grid=grid, r=r, c=c)
                    islands += 1 
        return islands
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    count += 1  # Increment count after a full DFS traversal
        return count


   

def dfs(grid, r, c):
    grid[r][c] = "0"  # Mark as visited
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
            dfs(grid, nr, nc)
# Example usage:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solution = Solution()
print(solution.numIslands(grid))  # Output: 3
