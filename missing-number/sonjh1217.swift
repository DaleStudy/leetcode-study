class Solution {
    // O(n) time / O(1) space
    func missingNumber(_ nums: [Int]) -> Int {
        let count = nums.count
        var expectedSum = count * (count + 1) / 2
        let actualSum = nums.reduce(0, +)
        return expectedSum - actualSum
    }
}
