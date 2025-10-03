class Solution {
    // Time O(n)
    // Space O(1)
    func missingNumber(_ nums: [Int]) -> Int {
        var sum = 0
        for i in 0..<nums.count {
            sum += i
            sum -= nums[i]
        }
        
        return sum + nums.count
    }
}
 
