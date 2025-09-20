class Solution {
    // Time (MN)
    // Space (MN)
    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: text2.count + 1),
                       count: text1.count + 1)
        for (i, char1) in text1.enumerated() {
            for (j, char2) in text2.enumerated() {
                if char1 == char2 {
                    dp[i + 1][j + 1] = dp[i][j] + 1
                } else {
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
                }
            }
        }
        
        return dp[text1.count][text2.count]
    }
}
 
