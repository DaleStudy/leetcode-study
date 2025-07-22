class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dictionary: [Int: Int] = [:]
        for (index, value) in nums.enumerated() {
            let difference = target - value
            if let otherIndex = dictionary[difference] {
                return [otherIndex, index]
            }
            dictionary[value] = index
        }
        return []
    }
}
 


