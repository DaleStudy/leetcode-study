class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        var answer: [Int] = Array(repeating: 1, count: nums.endIndex)
        for i in 1..<nums.endIndex {
            answer[i] = answer[i - 1] * nums[i - 1]
        }
        
        var suffix = 1
        for i in (0..<nums.endIndex).reversed() {
            answer[i] *= suffix
            suffix *= nums[i]
        }
        
        return answer
    }
}
 
