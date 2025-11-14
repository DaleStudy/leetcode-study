class Solution {
    func rob(_ nums: [Int]) -> Int {
        if nums.count < 3 {
            return nums.max()!
        }

        var expected = [Int]()
        expected.append(nums[0])
        expected.append(max(nums[0], nums[1]))

        for i in 2..<nums.count {
            let prev = expected[i - 1]
            let prevPrev = expected[i - 2]

            expected.append(max(prev, prevPrev + nums[i]))
        }

        return expected.removeLast()
    }
}
