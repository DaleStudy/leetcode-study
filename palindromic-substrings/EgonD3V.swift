import Foundation

class Solution {
    func countSubstrings(_ s: String) -> Int {
        return solve_2(s)
    }
    
    /*
         Runtime: 507 ms (Beats 5.07%)
         Analyze Complexity: O(n ** 3)
         Memory: 16.07 MB (Beats 80.43%)
     */
    func solve_1(_ s: String) -> Int {
        let sArray = Array(s)
        var count = 0
        for left in 0..<s.count {
            for right in left..<s.count {
                var isPalindrome = false
                for step in 0...(right-left) {
                    if sArray[left + step] != sArray[right - step] {
                        isPalindrome = true
                        break
                    }
                }

                count += isPalindrome ? 1 : 0
            }
        }
        
        return count
    }
    
    /*
         Runtime: 8 ms (Beats 37.68%)
         Analyze Complexity: O(n ** 2)
         Memory: 16.14 MB (Beats 72.46%)
     */
    func solve_2(_ s: String) -> Int {
        let sArray = Array(s)
        let n = sArray.count
        var count = 0
        
        for center in 0..<(2 * n - 1) {
            var left = center / 2
            var right = left + (center % 2)
            
            while 0 <= left && right < n && sArray[left] == sArray[right] {
                count += 1
                left -= 1
                right += 1
            }
        }
        
        return count
    }
    
    /*
         Runtime: 14 ms (Beats 30.43%)
         Analyze Complexity: O(n ** 2)
         Memory: 16.85 MB (Beats 13.04%)
     */
    func solve_3(_ s: String) -> Int {
        let sArray = Array(s)
        let n = sArray.count
        var dp = Array(repeating: Array(repeating: false, count: n), count: n)
        var count = 0
        
        for i in 0..<n {
            dp[i][i] = true
            count += 1
        }
        
        for i in 0..<(n - 1) {
            dp[i][i + 1] = sArray[i] == sArray[i + 1]
            count += dp[i][i + 1] == true ? 1 : 0
        }
        
        if n < 3 {
            return count
        }
        
        for length in 3..<(n + 1) {
            for left in 0..<(n - length + 1) {
                let right = left + length - 1
                dp[left][right] = dp[left + 1][right - 1] == true && sArray[left] == sArray[right]
                count += dp[left][right] == true ? 1 : 0
            }
        }
        
        return count
    }
}
