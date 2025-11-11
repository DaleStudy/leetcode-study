class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        let nums = nums.enumerated().sorted { $0.1 < $1.1 }

        for (index, num) in nums {
            let newTarget = target - num

            var left = 0
            var right = nums.count - 1

            while left <= right {
                let mid = (left + right) / 2

                if nums[mid].1 == newTarget && nums[mid].0 != index {
                    return [index, nums[mid].0]
                } else if nums[mid].1 < newTarget {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        return [0, 1]
    }
}