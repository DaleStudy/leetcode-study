class Solution {
    // Time O(1)
    // Space O(1)
    func reverseBits(_ n: Int) -> Int {
        var number = n
        var result = 0
        
        for i in 0..<32 {
            let bit = number & 1
            result = result << 1
            result = result | bit
            number = number >> 1
        }
        
        return result
    }
}
 
