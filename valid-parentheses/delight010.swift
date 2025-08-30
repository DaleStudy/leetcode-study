class Solution {
    func isValid(_ s: String) -> Bool {
        let dictionary: [Character: Character] = [")":"(", "]":"[", "}":"{"]
        var stack: [Character] = []
        for char in s {
            if let openBucket = dictionary[char] {
                if stack.isEmpty == false, stack.removeLast() == openBucket {
                    continue
                } else {
                    return false
                }
            }
            stack.append(char)
        }
        
        return stack.isEmpty
    }
}
 
