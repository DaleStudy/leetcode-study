class Solution {
    func climbStairs(_ n: Int) -> Int {
        var tables = [0, 1, 2]
        for i in 3...45 {
            let result = tables[i-1] + tables[i-2]
            tables.append(result)
        }

        return tables[n]
    }
}
