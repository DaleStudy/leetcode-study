class Solution {
    func countBits(_ n: Int) -> [Int] {
        // Time O(n log n)
        // Space O(1)
        var result: [Int] = []
        var count = 0
        var num = 0
        
        while num <= n {
            var temp = num
            
            while temp != 0 {
                if temp & 1 == 1 {
                    count += 1
                }
                temp >>= 1
            }
            
            result.append(count)
            count = 0
            num += 1
        }
        
        return result
    }
}
 
