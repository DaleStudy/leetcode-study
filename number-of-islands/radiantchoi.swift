class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        var grid = grid
        var result = 0
        
        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                // 임의의 인덱스 i, j에 대해 탐색 수행
                // 서로 떨어져 있는 섬도 모두 찾기 위해
                var isIsland = false
                traverse(i, j, &grid, &isIsland)

                if isIsland {
                    result += 1
                }
            }
        }

        return result
    }

    // DFS 함수
    func traverse(_ row: Int, _ col: Int, _ grid: inout [[Character]], _ isIsland: inout Bool) {
        // 인덱스가 유효한지 검사하고 유효하지 않으면 함수 종료
        guard (0..<grid.count) ~= row && (0..<grid[0].count) ~= col else { return }
        
        // 이미 방문한 곳, 원래 바다인 곳 등의 이유로 유효하지 않은 면적이면 함수 종료
        guard grid[row][col] != "0" else { return }

        // 방문 표시 + 유효한 면적을 발견했으므로 "섬이다" 라고 인정
        grid[row][col] = "0"
        isIsland = true

        // 상하좌우 탐색 - 한 번의 콜 스택에서 유효한 모든 연결된 면적을 찾아서 방문 표시
        traverse(row+1, col, &grid, &isIsland)
        traverse(row-1, col, &grid, &isIsland)
        traverse(row, col+1, &grid, &isIsland)
        traverse(row, col-1, &grid, &isIsland)
    }
}
