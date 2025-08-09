class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var maxSum = nums[0]
        var maxEndingHere = nums[0]
        for i in 1..<nums.count {
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            maxSum = max(maxSum, maxEndingHere)
        }
        return maxSum
    }
}
 
