class Solution {
    // O(n+m) (m = edges.count) time / O(n+m) space
    func countComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var graph = [[Int]](repeating: [], count: n)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        
        var visited = [Bool](repeating: false, count: n)
        var connectedComponents = 0
        
        for i in 0..<n {
            if visited[i] {
                continue
            }
            var queue = [Int]()
            queue.append(i)
            visited[i] = true
            var head = 0
                        
            while queue.count > head {
                let current = queue[head]
                head += 1
                
                for node in graph[current] {
                    if !visited[node] {
                        visited[node] = true
                        queue.append(node)
                    }
                }
            }
            connectedComponents += 1
        }
        
        return connectedComponents
    }
}

print(Solution().countComponents(3, [[0,1], [0,2]]))
print(Solution().countComponents(6, [[0,1], [1,2], [2, 3], [4, 5]]  ))
