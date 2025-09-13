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
    // O(V+E) time / O(V) space
    func cloneGraph(_ node: Node?) -> Node? {
        guard let node = node else {
            return nil
        }
        var newNodeByVal = [Int: Node]()
        return copy(node: node, newNodeByVal: &newNodeByVal)
    }
    
    func copy(node: Node, newNodeByVal: inout [Int: Node]) -> Node {
        if let node = newNodeByVal[node.val] {
            return node
        }
        var newNode = Node(node.val)
        newNodeByVal[node.val] = newNode
        
        for neighbor in node.neighbors {
            guard let neighbor = neighbor else {
                continue
            }
            let newNeighbor = copy(node: neighbor, newNodeByVal: &newNodeByVal)
            newNode.neighbors.append(newNeighbor)
        }
        return newNode
    }
}
