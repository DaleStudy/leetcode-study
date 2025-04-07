class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        let numbericSet = Set(nums)
        return numbericSet.count < nums.count
    }
}
