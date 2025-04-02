class Solution {
func rob(_ nums: [Int]) -> Int {
        let length = nums.count

        if length == 1 {
            return nums[0]
        }

        if length == 2 {
            return max(nums[0], nums[1])
        }

        var tables = Array(repeating: 0, count: length)
        tables[0] = nums[0]
        tables[1] = max(nums[0], nums[1])
        
        for i in 2..<length {
            tables[i] = max(nums[i]+tables[i-2], tables[i-1])
        }

        return tables[length-1]
    }
}
