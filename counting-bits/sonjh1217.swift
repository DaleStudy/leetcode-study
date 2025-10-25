class Solution {
    // Brute Force
    // O(nlogn) time / O(n) space
    func countBits(_ n: Int) -> [Int] {
        var numberOfOnes = [Int]()
        for i in 0...n {
            var numberOfOne = 0
            var i = i
            
            while i > 0 {
                numberOfOne += i & 1
                i >>= 1
            }
            
            numberOfOnes.append(numberOfOne)
        }
        
        return numberOfOnes
    }
    
    // Dynamic Programming
    // O(n) time / O(n) space
    func countBitsDP(_ n: Int) -> [Int] {
        var numberOfOnes = [Int](repeating: 0, count: n + 1)
        if n < 1 {
            return numberOfOnes
        }
        
        for i in 1...n {
            numberOfOnes[i] = numberOfOnes[i >> 1] + (i & 1)
        }
        return numberOfOnes
        
    }
}
