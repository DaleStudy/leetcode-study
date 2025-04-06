class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        let dict = nums.enumerated().reduce(into: [Int: Int]()) { initialValue, num in
            initialValue[num.element] = num.offset
        }
        
        for startIndex in 0..<nums.count {
            let findValue = target - nums[startIndex]
            if let endIndex = dict[findValue], startIndex != endIndex {
                return [startIndex, endIndex]
            }
        }
        
        return []
    }
}
