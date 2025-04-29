// time: O(N * M * 4^L) space: O(N * M + L)
// N 행 - M 열 - L word의 길이 (4방향을 탐색하기에 4^L)
class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        let words = Array(word)
        var visited = Array(repeating: Array(repeating: false, count: board[0].count), count: board.count)
        var startPoints = [(Int, Int)]()
        // 먼저 시작 가능한 인덱스들 찾기 - O(n^2)
        for i in board.indices {
            for j in board[0].indices {
                if board[i][j] == words[0] {
                    startPoints.append((i,j))
                }
            }
        }
        // 문자 찾아가기위한 DFS 내부함수 (backtracking)
        func dfs(_ row: Int, _ col: Int, _ index: Int) -> Bool {
            if row < 0 || col < 0 || row >= board.count || col >= board[0].count { return false }
            if visited[row][col] { return false }
            if board[row][col] != words[index] { return false }
            if index + 1 == word.count { return true }

            visited[row][col] = true

            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)] {
                let nextRow = row + dir.0
                let nextCol = col + dir.1
                if dfs(nextRow, nextCol, index + 1) {
                    return true
                }
            }

            visited[row][col] = false
            return false
        }
        // 문자 찾기
        for pos in startPoints {
            if dfs(pos.0, pos.1, 0) { return true }
        }
        return false
    }
}
