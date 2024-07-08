//  
//  261. Graph Valid Tree
//  https://leetcode.com/problems/graph-valid-tree/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/06.
//  

final class Solution {
  func validTree(_ n: Int, _ edges: [[Int]]) -> Bool {
    guard edges.count == n - 1
    else {
      return false
    }

    var dictionary: [Int: [Int]] = [:]
    var visited: Set<Int> = []

    for edge in edges {
      dictionary[edge[0], default: []].append(edge[1])
      dictionary[edge[1], default: []].append(edge[0])
    }

    func dfs(parent: Int, node: Int) {
      if visited.contains(node) {
        return
      }

      visited.insert(node)

      if let childNodes = dictionary[node] {
        for childNode in childNodes where childNode != parent {
          dfs(parent: node, node: childNode)
        }
      }
    }

    dfs(parent: -1, node: 0)

    return visited.count == n
  }
}
