class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let strings = s.filter { $0.isLetter || $0.isNumber }.lowercased()
        return String(strings.reversed()) == strings
    }
}
