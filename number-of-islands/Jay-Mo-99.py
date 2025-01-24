        #해석
        # r,c nested loop로 grid의 모든 element를 검사한다
        # 만약 1인 element를 만나면 sink함수를 호출한다
        #   -sink 함수는 해당 element를 0으로 만들고 해당 element의 좌,우,상,하가 1인지 체크한다
        #   -만약 1이 있다면 또 sink를 반복 호출하며 위의 검사를 반복한다.(1이 없을때까지)
        #   -만약 더이상 연결된 1이 없다면 재귀 호출 종료.
        # sink함수 종료 시시 nested loop로 돌아와서 이후후 1인 element를 찾는다. 
        # grid의 1이 sink로 모두 없어지면 return cls한다.  


        #Big O
        #- M: grid의 행의 갯수(r)
        #- N: grid의 열의 갯수(c)

        #Time Complexity: O(M*N) 
        #- for loop: 이중 루프로 grid의 모든 element에 도달 -> O(M*N) 
        #- sink(row,col): 최악의 경우 sink함수는 M*N번 호출 ->  O(M*N) 

        #Space Complexity: O(M∗N)
        #- sink 재귀호출: 
        #  최악의 경우 sink함수는 스택에 M*N번 재귀 호출 당한다.
        #  스택에 해당 메모리 누적(재귀 호출 스택의 깊이가 M*N) -> O(M*N) 
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(row, col):
            grid[row][col] = "0"

            for r, c in [
                (row, col - 1), #Left
                (row, col + 1), #Right
                (row - 1, col), #Up
                (row + 1, col), #Down
            ]:
                # If the neighbor cell is within bounds and is land ("1"), sink it recursively.
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    if grid[r][c] == "1":
                        sink(r, c) 

        cnt = 0 # Count the number of islands.
        # Loop through every cell in the grid.
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    cnt += 1  
                    sink(r, c) ## Sink the entire island by converting all connected "1"s to "0"s.
        return cnt
    
mySolution = Solution()
mySolution.numIslands(
    [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
)



