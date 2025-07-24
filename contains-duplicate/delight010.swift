class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var dictionary: [Int: Int] = [:]
        for (index, num) in nums.enumerated() {
            if let value = dictionary[num], value != index {
                return true
            }
            dictionary[num] = index
        }
        return false
    }
}
 
