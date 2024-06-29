//  
//  133. Clone Graph
//  https://leetcode.com/problems/clone-graph/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/28.
//  

/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var neighbors: [Node?]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.neighbors = []
 *     }
 * }
 */

class Solution {
  var cache: [Int: Node] = [:]

  func cloneGraph(_ originalNode: Node?) -> Node? {
    guard let originalNode
    else {
      return nil
    }

    guard cache[originalNode.val] == nil
    else { return cache[originalNode.val]! }

    let node = Node(originalNode.val)
    cache[originalNode.val] = node


    node.neighbors = originalNode.neighbors.map(cloneGraph)

    return node
  }
}
