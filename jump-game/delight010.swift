class Solution {
    // Time O(n)
    // Space O(1)
    func canJump(_ nums: [Int]) -> Bool {
        var maxReachIndex = 0
        for i in 0..<nums.count {
            if i > maxReachIndex {
                return false
            }
            maxReachIndex = max(maxReachIndex, nums[i] + i)
        }
        
        return maxReachIndex >= nums.count - 1
    }
}
 
