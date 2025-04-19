///53. Maximum Subarray
///정수 배열 Nums가 주어질때, subarray들 중에서 가장 합이 큰걸 구하고 그 합을 반환하라
///subarray: 비지 않은 연속된 요소들의 배열


class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        
        var currentSum = nums[0]
        var maxSum = nums[0]
        
        for num in nums.dropFirst() {
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        }
        
        return maxSum
    }
}
