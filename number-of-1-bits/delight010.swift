class Solution {
    func hammingWeight(_ n: Int) -> Int {
        var number = n
        var answer = 0
        while number > 0 {
            if number & 1 == 1 {
                answer += 1
            }
            number = number >> 1
        }
        return answer
    }
}
 
