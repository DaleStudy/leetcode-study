class Solution {
    func isValid(_ s: String) -> Bool {
        let pair: [Character: Character] = [
            "(": ")",
            "[": "]",
            "{": "}"
        ]
        
        var stack: [Character] = []
        
        for char in s {
            if pair.keys.contains(char) {
                stack.append(char)
            } else {
                if stack.isEmpty || pair[stack.removeLast()] != char {
                    return false
                }
            }
        }
        
        return stack.isEmpty
    }
}
