class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let nums = nums.sorted()
        var answer: Set<[Int]> = []
        for (index, num) in nums.enumerated() {
            var leftIndex = index + 1
            var rightIndex = nums.endIndex - 1
            while leftIndex < rightIndex {
                let sum = num + nums[leftIndex] + nums[rightIndex]
                if sum == 0 {
                    answer.insert([num, nums[leftIndex], nums[rightIndex]])
                    leftIndex += 1
                    rightIndex -= 1
                } else if sum < 0 {
                    leftIndex += 1
                } else if sum > 0 {
                    rightIndex -= 1
                }
            }
        }
        
        return Array(answer)
    }
}
 
