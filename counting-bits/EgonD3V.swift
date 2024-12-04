import Foundation

class Solution {
    func countBits(_ n: Int) -> [Int] {
        return solve_2(n)
    }
    
    /*
        **내장함수를 사용한 풀이**
     
        Runtime: 37 ms (Beats 49.12%)
        Time Complexity: O(n * log n)
            - 길이가 n인 range를 순회하므로 O(n)
            - 정수에 대해 non zero bit를 세는데 O(log n)
            > O(n * log n)
        Space Complexity: O(n)
            - 배열에 값을 저장하며 크기가 n이 되므로 O(n)
        Memory: 20.86 MB (Beats 90.106%)
    */
    func solve_1(_ n: Int) -> [Int] {
        var result: [Int] = []
        for num in 0...n {
            result.append(num.nonzeroBitCount)
        }
        return result
    }
    
    /*
        ** Brian Kernighan's Algorithm을 사용한 풀이 **
     
        Runtime: 39 ms (Beats 42.11%)
        Time Complexity: O(n * log n)
            - 길이가 n인 range를 순회하므로 O(n)
            - bitCountWithBrianKernighan 에서 내부 while문 실행마다 num이 절반으로 줄어드므로, 실행횟수는 O(log n)
            > O(n * log n)
        Space Complexity: O(n)
            - 배열에 값을 저장하며 크기가 n이 되므로 O(n)
        Memory: 16.01 MB (Beats 67.84%)
    */
    func solve_2(_ n: Int) -> [Int] {
        
        func bitCountWithBrianKernighan(_ num: Int) -> Int {
            var num = num
            var bitCount = 0
            while 0 < num {
                num &= (num - 1)
                bitCount += 1
            }
            
            return bitCount
        }
        
        var result: [Int] = []
        for num in 0...n {
            result.append(bitCountWithBrianKernighan(num))
        }
        return result
    }
    
    /*
        ** MSB에 대해 DP를 사용한 풀이 **
        > num의 비트 카운트 = MSB의 비트 카운트(1 고정) + (num - msb)의 비트 카운트
     
        Runtime: 36 ms (Beats 58.48%)
        Time Complexity: O(n)
            - 0부터 n까지 range를 순회하므로 O(n)
            > O(n)
        Space Complexity: O(n)
            - 길이가 n인 dp 배열을 저장하므로 O(n)
        Memory: 21.15 MB (Beats 67.84%)
    */
    func solve_3(_ n: Int) -> [Int] {
        guard 1 <= n else { return [0] }
        
        var dp = [Int](repeating: 0, count: n + 1)
        var msb = 1
        for num in 1...n {
            if msb << 1 == num {
                msb = num
            }
            
            dp[num] = 1 + dp[num - msb]
        }
        
        return dp
    }
    
    /*
        ** LSB에 대해 DP를 사용한 풀이 **
        > num의 비트 카운트 = num을 right shift한 숫자의 비트 카운트 + LSB의 비트 카운트(1 또는 0)
     
        Runtime: 28 ms (Beats 97.08%)
        Time Complexity: O(n)
            - 0부터 n까지 range를 순회하므로 O(n)
            > O(n)
        Space Complexity: O(n)
            - 길이가 n인 dp 배열을 저장하므로 O(n)
        Memory: 21.26 MB (Beats 53.80%)
    */
    func solve_4(_ n: Int) -> [Int] {
        guard 1 <= n else { return [0] }
        
        var dp = [Int](repeating: 0, count: n + 1)
        for num in 1...n {
            dp[num] = dp[num >> 1] + (num & 1)
        }
        
        return dp
    }
}

let solution = Solution()
print(solution.solve_4(0))
