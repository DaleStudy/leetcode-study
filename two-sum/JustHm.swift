class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        for index in 0..<nums.count {
            if let item = dict[nums[index]] {
                return [item, index]
            }
            else { dict[target - nums[index]] = index }
        }
        return []
    }
}
