class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        var answer = [Int]()
        var product:Int = 1
        for i in (0..<nums.count) {
            if i > 0 {
                product *= nums[i-1]
            }
            answer.append(product)
        }

        product = 1
        for i in (1..<nums.count) {
            product *= nums[nums.count-i]
            answer[nums.count-1-i] *= product
        }
        
        return answer
        
        //시간 복잡도 O(n)
        //공간 복잡도 O(n)
    }
}

