class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        nums.count != Set(nums).count
    }
}
