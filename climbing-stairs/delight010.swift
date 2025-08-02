class Solution {
    func climbStairs(_ n: Int) -> Int {
        var dictionary: [Int: Int] = [:]
        for i in 1...n {
            if i < 3 {
                dictionary[i] = i
            } else {
                if let value1 = dictionary[i - 1],
                   let value2 = dictionary[i - 2] {
                    dictionary[i] = value1 + value2
                }
            }
        }
        return dictionary[n] ?? 0
    }
}
 
