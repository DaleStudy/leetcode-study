class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        if candidates.filter { $0 > target }.count == candidates.count {
            return []
        }
        
        var result: [[Int]] = []
        var current: [Int] = []
        
        func backtrack(_ start: Int, _ remain: Int) {
            if remain == 0 {
                result.append(current)
                return
            }
            
            if remain < 0 {
                return
            }
            
            for i in start..<candidates.count {
                current.append(candidates[i])
                backtrack(i, remain - candidates[i])
                current.removeLast()
            }
        }
        
        backtrack(0, target)
        
        return result
    }
}
