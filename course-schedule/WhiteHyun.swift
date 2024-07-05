//  
//  207. Course Schedule
//  https://leetcode.com/problems/course-schedule/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/30.
//  

class Solution {
  func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
    var graph: [Int: [Int]] = [:]
    var visited: [Int: Bool] = [:]

    // 그래프 구성
    for prereq in prerequisites {
      let course = prereq[0]
      let prerequisite = prereq[1]
      graph[course, default: []].append(prerequisite)
    }

    func dfs(_ course: Int) -> Bool {
      if visited[course] == true { return false }
      if visited[course] == false { return true }

      visited[course] = true

      if let prerequisites = graph[course] {
        for prereq in prerequisites {
          if !dfs(prereq) { return false }
        }
      }

      visited[course] = false
      return true
    }

    for course in 0 ..< numCourses {
      if !dfs(course) { return false }
    }

    return true
  }
}
