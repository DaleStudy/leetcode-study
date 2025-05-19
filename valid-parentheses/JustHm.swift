// time: O(n) space: O(n)
class Solution {
    func isValid(_ s: String) -> Bool {
        var answer = [Character]()
        for char in s {
            if let recent = answer.last {
                if char == ")" && recent == "(" {
                    answer.removeLast()
                    continue
                }
                else if char == "]" && recent == "[" {
                    answer.removeLast()
                    continue
                }
                else if char == "}" && recent == "{" {
                    answer.removeLast()
                    continue
                }
            }
            answer.append(char)
        }
        return answer.isEmpty
    }
}
