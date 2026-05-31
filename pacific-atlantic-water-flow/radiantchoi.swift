// 힌트를 받은 아이디어: 특정 칸에서 흘러내려가는 것이 아니라, 바다에서부터 거슬러 올라가는 것을 계산하면 어떨까?

class Solution {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        var result = [[Int]]()
        var pacificMap = Array(repeating: Array(repeating: false, count: heights[0].count), count: heights.count)
        var atlanticMap = Array(repeating: Array(repeating: false, count: heights[0].count), count: heights.count)

        for k in 0..<heights[0].count {
            traverse(heights, 0, k, 0, &pacificMap)
        }

        for l in 0..<heights.count {
            traverse(heights, l, 0, 0, &pacificMap)
        }

        for m in 0..<heights[0].count {
            traverse(heights, heights.count - 1, m, 0, &atlanticMap)
        }

        for n in 0..<heights.count {
            traverse(heights, n, heights[0].count - 1, 0, &atlanticMap)
        }

        for i in 0..<heights.count {
            for j in 0..<heights[i].count {
                if pacificMap[i][j] && atlanticMap[i][j] {
                    result.append([i, j])
                }
            }
        }

        return result
    }

    func traverse(_ heights: [[Int]], _ row: Int, _ col: Int, _ previous: Int, _ reachabilities: inout [[Bool]]) {
        guard (0..<heights.count) ~= row && (0..<heights[0].count) ~= col else { return }

        guard heights[row][col] >= previous else { return }
        guard !reachabilities[row][col] else { return }

        reachabilities[row][col] = true

        traverse(heights, row - 1, col, heights[row][col], &reachabilities)
        traverse(heights, row + 1, col, heights[row][col], &reachabilities)
        traverse(heights, row, col - 1, heights[row][col], &reachabilities)
        traverse(heights, row, col + 1, heights[row][col], &reachabilities)
    }
}
