//  
//  323. Number of Connected Components in an Undirected Graph
//  https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/06.
//  

final class Solution {
  func countComponents(_ n: Int, _ edges: [[Int]]) -> Int {
    var visited: Set<Int> = []
    var count = 0

    var graph: [Int: [Int]] = [:]

    for edge in edges {
      graph[edge[0], default: []].append(edge[1])
      graph[edge[1], default: []].append(edge[0])
    }

    func dfs(_ node: Int) {
      if visited.contains(node) {
        return
      }

      visited.insert(node)

      for nextNode in graph[node, default: []] {
        dfs(nextNode)
      }
    }

    for node in 0 ..< n where !visited.contains(node) {
      count += 1
      dfs(node)
    }

    return count
  }
}
