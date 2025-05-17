class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        guard !grid.isEmpty else { return 0 }
        
        let rows = grid.count
        let colums = grid[0].count
        var visited = grid
        var islandCount = 0
        
        func dfs(_ row: Int, _ col: Int) {
            guard row >= 0 && row < rows && col >= 0 && col < colums && visited[row][col] == "1" else {
                return
            }
            
            visited[row][col] = "0"
            
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        }
        
        for row in 0..<rows {
            for col in 0..<colums {
                if visited[row][col] == "1" {
                    islandCount += 1
                    dfs(row, col)
                }
            }
        }
        
        return islandCount
    }
}
