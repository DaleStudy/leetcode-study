class Solution {
    // Time O(V+E)
    // Space O(V)
    func cloneGraph(_ node: Node?) -> Node? {
        guard let node = node else { return nil }
        
        var visited: [Int: Node] = [:]
        var queue: [Node] = []
        
        let firstNode = Node(node.val)
        visited[node.val] = firstNode
        
        queue.append(node)
        
        while !queue.isEmpty {
            let currentNode = queue.removeFirst()
            
            for neighbor in currentNode.neighbors {
                guard let neighbor = neighbor else { continue }
                
                if let clonedNeighbor = visited[neighbor.val] {
                    visited[currentNode.val]!.neighbors.append(clonedNeighbor)
                } else {
                    visited[neighbor.val] = Node(neighbor.val)
                    visited[currentNode.val]!.neighbors.append(visited[neighbor.val])
                    queue.append(neighbor)
                }
            }
        }
        
        return firstNode
    }
}
 
