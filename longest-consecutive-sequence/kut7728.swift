class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let numSet = Set(nums)
        var longest = 0

        for num in numSet {
            // 연속 수열의 시작점인지 확인
            if !numSet.contains(num - 1) {
                var currentNum = num
                var currentStreak = 1

                while numSet.contains(currentNum + 1) {
                    currentNum += 1
                    currentStreak += 1
                }

                longest = max(longest, currentStreak)
            }
        }

        return longest
    }
}
