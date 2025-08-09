class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var result: [[Int]] = []
        var current: [Int] = []
        findCombination(0, target, candidates, &current, &result)
        return result
    }
    
    func findCombination(_ index: Int, _ target: Int, _ candidates: [Int], _ current: inout [Int], _ result: inout [[Int]]) {
        if target == 0 {
            result.append(current)
            return
        }
        
        for i in index..<candidates.count {
            if candidates[i] <= target {
                current.append(candidates[i])
                findCombination(i, target - candidates[i], candidates, &current, &result)
                current.removeLast()
            }
        }
    }
}
 
