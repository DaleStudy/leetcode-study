class Solution {
    // O(m*n) time / O(m*n) space
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        var result = [[Int]]()
        guard let first = heights.first else {
            return result
        }
        let m = heights.count
        let n = first.count
        
        var goesPacific = Array(repeating: Array(repeating: false, count: n), count: m)
        var goesAtlantic = Array(repeating: Array(repeating: false, count: n), count: m)
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        func dfs(i: Int, j: Int, goes: inout [[Bool]]) {
            if goes[i][j] {
                return
            }
            goes[i][j] = true
            
            for (di, dj) in directions {
                let ni = i + di
                let nj = j + dj
                if ni >= 0
                    && ni < m
                    && nj >= 0
                    && nj < n
                    && heights[ni][nj] >= heights[i][j]  {
                    dfs(i: ni, j: nj, goes: &goes)
                }
            }
        }
        
        for i in 0..<m {
            dfs(i: i, j: 0, goes: &goesPacific)
            dfs(i: i, j: n-1, goes: &goesAtlantic)
        }
        
        for j in 0..<n {
            dfs(i: 0, j: j, goes: &goesPacific )
            dfs(i: m-1, j: j, goes: &goesAtlantic )
        }
        
        for i in 0..<m {
            for j in 0..<n {
                if goesPacific[i][j] && goesAtlantic[i][j] {
                    result.append([i, j])
                }
            }
        }
        return result
    }
}
