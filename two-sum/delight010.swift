class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dictionary: [Int: Int] = [:]
        for (index, value) in nums.enumerated() {
            // nums배열의 개수만큼 반복합니다. O(n)
            let difference = target - value
            if let otherIndex = dictionary[difference] {
                return [otherIndex, index]
            }
            dictionary[value] = index
        }
        return []
    }
}
 
