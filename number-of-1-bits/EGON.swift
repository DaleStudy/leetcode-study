import Foundation

class Solution {
    func hammingWeight(_ n: Int) -> Int {
        return solve_2(n)
    }
    
    /*
        Runtime: 5 ms (Beats 38.73%)
        Analyze Complexity: O(k), k는 2진수의 1의 갯수
        Memory: 14.88 MB (Beats 98.27%)
     */
    func solve_1(_ n: Int) -> Int {
        return n.nonzeroBitCount
    }
    
    /*
        Runtime: 3 ms (Beats 65.90%)
        Analyze Complexity: O(k), k는 2진수의 1의 갯수
        Memory: 15.08 MB (Beats 89.02%)
     */
    func solve_2(_ n: Int) -> Int {
        var num = n
        var hammingWeight = 0
        while 0 < num {
            num &= num - 1
            hammingWeight += 1
        }
        
        return hammingWeight
    }
}
