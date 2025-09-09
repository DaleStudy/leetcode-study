class Solution {
    // O(1) time / O(1) space
    func reverseBits(_ n: Int) -> Int {
        var number = n
        var reversed = 0
        
        for _ in 0..<32 {
            reversed <<= 1
            reversed |= (number & 1)
            number >>= 1
        }
        return reversed
    }
}
