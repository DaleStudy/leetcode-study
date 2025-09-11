class Solution {
    func countSubstrings(_ s: String) -> Int {
        let charArray = Array(s)
        var count = 0
        
        for i in 0..<charArray.count {
            count += countPalindrome(charArray, i, i)
            count += countPalindrome(charArray, i, i + 1)
        }
        
        return count
    }
    
    private func countPalindrome(_ s: [Character], _ left: Int, _ right: Int) -> Int {
        var left = left
        var right = right
        var count = 0
        
        while left >= 0 && right < s.count {
            if s[left] == s[right] {
                count += 1
            } else {
                break
            }
            
            left -= 1
            right += 1
        }
        
        return count
    }
}
 
