class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        let length = nums.count
        var result = Array(repeating: 1, count: length)
        var leftProduct = 1
        for i in 0..<length {
            result[i] = leftProduct
            leftProduct *= nums[i]
        }
        
        var rightProduct = 1
        for i in (0..<length).reversed() {
            result[i] *= rightProduct
            rightProduct *= nums[i]
        }
        
        return result
    }
}
