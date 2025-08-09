class Solution {
    func numDecodings(_ s: String) -> Int {
        var array = Array(s)
        var dp: [Int: Int] = [array.count: 1]
        for i in stride(from: array.count - 1, to: -1, by: -1) {
            if array[i] == "0" {
                dp[i] = 0
            } else {
                dp[i] = dp[i + 1]
            }

            if i + 1 < array.count && (array[i] == "1" || array[i] == "2" && "0123456".contains(array[i + 1])) {
                dp[i, default: 0] += dp[i + 2] ?? 0
            }
        }
        return dp[0]!
    }
}
 
