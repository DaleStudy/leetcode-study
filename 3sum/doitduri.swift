import Foundation

class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        var result = [[Int]]()
        let sortedNums = nums.sorted()
        
        for i in 0..<sortedNums.count - 2 {
            if i > 0 && sortedNums[i] == sortedNums[i - 1] {
                continue
            }
            
            var leftNumber = i + 1
            var rightNumber = sortedNums.count - 1
            
            while leftNumber < rightNumber {
                let sum = sortedNums[i] + sortedNums[leftNumber] + sortedNums[rightNumber]
                
                if sum < 0 {
                    leftNumber += 1
                } else if sum > 0 {
                    rightNumber -= 1
                } else {
                    result.append([sortedNums[i], sortedNums[leftNumber], sortedNums[rightNumber]])
                    
                    while leftNumber < rightNumber && sortedNums[leftNumber] == sortedNums[leftNumber + 1] {
                        leftNumber += 1
                    }
                    
                    while leftNumber < rightNumber && sortedNums[rightNumber] == sortedNums[rightNumber - 1] {
                        rightNumber -= 1
                    }
                    
                    leftNumber += 1
                    rightNumber -= 1
                }
            }
        }
        
        return result
    }
}

