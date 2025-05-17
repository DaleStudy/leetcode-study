class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let answer = s.lowercased().filter {
            if $0.isLetter || $0.isNumber {
                return true
            }
            return false
        }
        return answer == String(answer.reversed()) ? true : false
    }
}
