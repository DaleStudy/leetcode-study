//  
//  79. Word Search
//  https://leetcode.com/problems/word-search/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/28.
//  

class Solution {
  func exist(_ board: [[Character]], _ word: String) -> Bool {
    let rows = board.count
    let cols = board[0].count
    let word = Array(word)
    var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)

    for row in 0 ..< rows {
      for col in 0 ..< cols {
        if board[row][col] == word[0], dfs(board, word, row, col, 0, &visited) {
          return true
        }
      }
    }

    return false
  }

  private func dfs(_ board: [[Character]], _ word: [Character], _ row: Int, _ col: Int, _ index: Int, _ visited: inout [[Bool]]) -> Bool {
    if index == word.count {
      return true
    }

    if row < 0 || row >= board.count || col < 0 || col >= board[0].count || visited[row][col] || board[row][col] != word[index] {
      return false
    }

    visited[row][col] = true

    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for (dx, dy) in directions {
      if dfs(board, word, row + dx, col + dy, index + 1, &visited) {
        return true
      }
    }

    visited[row][col] = false
    return false
  }
}
