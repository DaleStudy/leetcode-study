class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var adj: [[Int]] = Array(repeating: [], count: numCourses)
        for ab in prerequisites {
            adj[ab[0]].append(ab[1])
        }
        var visited = Array(repeating: 0, count: numCourses)
        var stack = Array(0..<numCourses)
        while !stack.isEmpty {
            let u = stack.last!
            if visited[u] == 2 {
                stack.removeLast()
                continue
            } else if visited[u] == 1 {
                visited[u] = 2
                stack.removeLast()
                continue
            }
            visited[u] = 1
            for v in adj[u] {
                if visited[v] == 1 {
                    return false
                }
                if visited[v] == 2 {
                    continue
                }
                stack.append(v)
            }
        }
        return true
    }
}
