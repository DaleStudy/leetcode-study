class Solution {
    // O(m*n) time / O(m*n) space
    func pacificAtlanticBFS(_ heights: [[Int]]) -> [[Int]] {
        var result = [[Int]]()
        guard let first = heights.first else {
            return result
        }
        let m = heights.count
        let n = first.count
        
        var goesPacific = Array(repeating: Array(repeating: false, count: n), count: m)
        var goesAtlantic = Array(repeating: Array(repeating: false, count: n), count: m)
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        func bfs(queue: [(Int, Int)], goes: inout [[Bool]]) {
            var queue = queue
            var head = 0
            for (i, j) in queue {
                goes[i][j] = true
            }
            
            while head < queue.count {
                let (i, j) = queue[head]
                head += 1
                
                for (di, dj) in directions {
                    let ni = i + di
                    let nj = j + dj
                    if ni >= 0
                        && ni < m
                        && nj >= 0
                        && nj < n
                        && !goes[ni][nj]
                        && heights[ni][nj] >= heights[i][j]  {
                        goes[ni][nj] = true
                        queue.append((ni, nj))
                    }
                }
            }
        }
        
        var pacificStarts = [(Int, Int)]()
        var atlanticStarts = [(Int, Int)]()
        for i in 0..<m {
            pacificStarts.append((i, 0))
            atlanticStarts.append((i, n-1))
        }
        
        for j in 0..<n {
            pacificStarts.append((0, j))
            atlanticStarts.append((m-1, j))
        }
        
        bfs(queue: pacificStarts, goes: &goesPacific)
        bfs(queue: atlanticStarts, goes: &goesAtlantic)
        
        for i in 0..<m {
            for j in 0..<n {
                if goesPacific[i][j] && goesAtlantic[i][j] {
                    result.append([i, j])
                }
            }
        }
        return result
    }
    
    // O(m*n) time / O(m*n) space
    func pacificAtlanticDFS(_ heights: [[Int]]) -> [[Int]] {
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
