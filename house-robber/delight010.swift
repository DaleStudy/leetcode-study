class Solution {
    func rob(_ nums: [Int]) -> Int {
        var sum1 = 0
        var sum2 = 0
        for num in nums {
            // for문을 통해 루프.
            // 시간복잡도는 O(n)
            let temp = max(num + sum1, sum2)
            sum1 = sum2
            sum2 = temp
        }
        return sum2
    }
}
 
