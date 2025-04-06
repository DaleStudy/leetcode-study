class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        var result = 1
        var maxResult = 1
        let sortedNums = nums.sorted()
        
        guard var previous = sortedNums.first else {
            return 0
        }
        
        for index in 1..<sortedNums.count {
            let next = sortedNums[index]
            
            if previous == next { // 숫자가 같으면 카운팅하지 않는다.
                continue
            }
            
            if previous + 1 == next {
                result += 1
                maxResult = max(maxResult, result)
            } else {
                result = 1
            }
            
            previous = next
        }
        
        return maxResult
    }
}
