//  
//  200. Number of Islands
//  https://leetcode.com/problems/number-of-islands/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/28.
//  

class Solution {
  func numIslands(_ grid: [[Character]]) -> Int {
    var visited: [[Bool]] = .init(
      repeating: .init(repeating: false, count: grid[0].count),
      count: grid.count
    )
    var islands = 0

    for row in 0 ..< grid.count {
      for col in 0 ..< grid[row].count where grid[row][col] == "1" && !visited[row][col] {
        visited[row][col] = true
        dfs(grid, &visited, row, col)
        islands += 1
      }
    }

    return islands
  }

  private func dfs(
    _ grid: [[Character]],
    _ visited: inout [[Bool]],
    _ x: Int,
    _ y: Int
  ) {
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
      let nx = dx + x
      let ny = dy + y
      guard grid.indices ~= nx,
            grid[x].indices ~= ny,
            visited[nx][ny] == false,
            grid[nx][ny] == "1"
      else {
        continue
      }
      visited[nx][ny] = true
      dfs(grid, &visited, nx, ny)
    }
  }
}
