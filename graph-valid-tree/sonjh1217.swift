import Foundation

class Solution {
    // O(n) time / O(n) space
    func validTree(_ n: Int, _ edges: [[Int]]) -> Bool {
        guard edges.count == n - 1 else {
            return false
        }
        
        var connectedNodes = Array(repeating: [Int](), count: n)
                
        for edge in edges {
            connectedNodes[edge[0]].append(edge[1])
            connectedNodes[edge[1]].append(edge[0])
        }
        
        var isVisiteds = Array(repeating: false, count: n)
        var head = 0
        var queue = [0]
        isVisiteds[0] = true
        
        while head < queue.count {
            let currentNode = queue[head]
            head += 1
            
            for node in connectedNodes[currentNode] {
                guard !isVisiteds[node] else { continue }
                
                isVisiteds[node] = true
                queue.append(node)
            }
        }
        
        return isVisiteds.allSatisfy { $0 }
    }
}
