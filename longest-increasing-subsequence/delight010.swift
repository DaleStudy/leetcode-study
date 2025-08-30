class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var tails: [Int] = []
        for num in nums {
            if let lastValue = tails.last {
                if num > lastValue {
                    tails.append(num)
                } else {
                    if let index = tails.firstIndex(where: { $0 >= num }) {
                        tails[index] = num
                    }
                }
            } else {
                tails.append(num)
            }
        }
        
        return tails.count
    }
}
 
