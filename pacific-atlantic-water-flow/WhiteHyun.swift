//  
//  417. Pacific Atlantic Water Flow
//  https://leetcode.com/problems/pacific-atlantic-water-flow/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/29.
//  

class Solution {
  func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
    var result: [[Int]] = []
    for i in heights.indices {
      for j in heights[i].indices where isValid(i, j, heights) {
        result.append([i, j])
      }
    }

    return result
  }

  private func isValid(_ i: Int, _ j: Int, _ heights: [[Int]]) -> Bool {
    var visited: [[Bool]] = .init(
      repeating: .init(repeating: false, count: heights[i].count),
      count: heights.count
    )
    visited[i][j] = true
    var pacificOceanFlag = i == 0 || j == 0
    var atlanticOceanFlag = i == heights.count - 1 || j == heights[i].count - 1

    func dfs(_ x: Int, _ y: Int) {
      if pacificOceanFlag, atlanticOceanFlag { return }
      for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
        let nx = x + dx
        let ny = y + dy

        guard heights.indices ~= nx,
              heights[nx].indices ~= ny,
              visited[nx][ny] == false,
              heights[nx][ny] <= heights[x][y]
        else {
          continue
        }

        visited[nx][ny] = true
        if nx == 0 || ny == 0 {
          pacificOceanFlag = true
        }
        if nx == heights.endIndex - 1 || ny == heights[nx].endIndex - 1 {
          atlanticOceanFlag = true
        }

        dfs(nx, ny)
      }
    }

    dfs(i, j)

    return pacificOceanFlag && atlanticOceanFlag
  }
}
