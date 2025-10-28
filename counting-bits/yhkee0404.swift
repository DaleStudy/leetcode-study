class Solution {
    func countBits(_ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n + 1) // S(n) = O(n)
        for i in 1..<n+1 { // T(n) = O(n)
            ans[i] = ans[i >> 1] + (i & 1)
        }
        return ans
    }
}
