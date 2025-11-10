class Solution {
    // time O(n) / space O(n)
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var numSet = Set<Int>()
        for num in nums {
            if numSet.contains(num) {
                return true
            }
            numSet.insert(num)
        }

        return false
    }
}
