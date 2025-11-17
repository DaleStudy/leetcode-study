class Solution {
    // Time  O(V + E)
    // Space  O(V + E)
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var indegree: [Int] = Array(repeating: 0, count: numCourses)
        var queue: [Int] = []
        var graph: [[Int]] = Array(repeating: [], count: numCourses)
        
        for i in 0..<prerequisites.count {
            let degree = prerequisites[i].first!
            let graphIndex = prerequisites[i][1]
            indegree[degree] += 1
            graph[graphIndex].append(degree)
        }
        
        for i in 0..<indegree.count {
            if indegree[i] == 0 {
                queue.append(i)
            }
        }
        
        var count = 0
        
        while !queue.isEmpty {
            let current = queue.removeFirst()
            count += 1
            for i in graph[current] {
                indegree[i] -= 1
                if indegree[i] == 0 {
                    queue.append(i)
                }
            }
        }
        
        return count == numCourses
    }
}
 
