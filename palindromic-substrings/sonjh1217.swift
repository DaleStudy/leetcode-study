class Solution {
    //dynamic programming
    // O(n^2) time / O(n^2) space
    func countSubstrings1(_ s: String) -> Int {
        var count = 0
        var characters = Array(s)
        var isPalindromes = Array(repeating: Array(repeating: false, count: characters.count), count: characters.count)
        
        for i in 0..<characters.count {
            isPalindromes[i][i] = true
            count += 1
        }
        
        for right in 1..<characters.count {
            for left in 0..<right {
                if characters[left] == characters[right]
                    && (isPalindromes[left+1][right-1] || right-left <= 2) {
                    isPalindromes[left][right] = true
                    count += 1
                }
            }
        }
        
        return count
    }
    
    //two pointers
    // O(n^2) time / O(n) space
    func countSubstrings2(_ s: String) -> Int {
        var count = 0
        var characters = Array(s)
        var left: Int
        var right: Int
        
        for i in 0..<characters.count{
            left = i
            right = i
            
            while left >= 0
                    && right < characters.count
                    && characters[left] == characters[right] {
                count += 1
                
                left -= 1
                right += 1
            }
            
            left = i
            right = i+1
            
            while left >= 0
                    && right < characters.count
                    && characters[left] == characters[right] {
                count += 1
                
                left -= 1
                right += 1
            }
        }
        
        return count
    }
    
}

