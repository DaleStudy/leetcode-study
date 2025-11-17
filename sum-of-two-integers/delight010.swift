class Solution {
    // Time O(log n)
    // Space O(1)
    func getSum(_ a: Int, _ b: Int) -> Int {
        var a = a
        var b = b
        
        while b != 0 {
            var sum = a ^ b
            var carry = (a & b) << 1
            a = sum
            b = carry
        }
        
        return a
    }
}
 
