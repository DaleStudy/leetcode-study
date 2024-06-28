//  
//  39. Combination Sum
//  https://leetcode.com/problems/combination-sum/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/27.
//  

class Solution {
  func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
    let sortedCandidates = candidates.sorted()
    var answer: [[Int]] = []

    func backtrack(_ sum: Int, _ start: Int, _ current: [Int]) {
      if sum == target {
        answer.append(current)
        return
      }

      if sum > target {
        return
      }

      for i in start ..< sortedCandidates.count {
        let newSum = sum + sortedCandidates[i]
        if newSum > target {
          break
        }
        backtrack(newSum, i, current + [sortedCandidates[i]])
      }
    }

    backtrack(0, 0, [])
    return answer
  }
}
