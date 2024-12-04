import Foundation

class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        return solve_2(nums)
    }
    
    /*
         Runtime: 246 ms (Beats 68.44%)
         Analyze Complexity: O(n)
         Memory: 19.94 MB (Beats 76.01%)
     */
    func solve_1(_ nums: [Int]) -> Bool {
        return nums.count != Set(nums).count
    }
    
    /*
         Runtime: 240 ms (Beats 90.56%)
         Analyze Complexity: O(n)
         Memory: 22.56 MB (Beats 33.43%)
     */
    func solve_2(_ nums: [Int]) -> Bool {
        var counter: [Int: Bool] = [:]
        for num in nums {
            if counter[num] != nil {
                return true
            } else {
                counter[num] = true
            }
        }
        
        return false
    }
}
