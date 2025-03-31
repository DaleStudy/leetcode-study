///  Time, Space Complexity O(N)

class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var seen = Set<Int>()
        for num in nums {
            if seen.contains(num) {
                return true
            }
            seen.insert(num)
        }
        return false
    }
}
