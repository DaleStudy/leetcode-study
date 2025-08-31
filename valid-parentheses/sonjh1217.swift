class Solution {
    func isValid (_ s: String) -> Bool {
        var brackets: [Character: Character] = ["(": ")", "[": "]", "{": "}"]
        var closers = [Character]()
        
        for character in s {
            if let closer = brackets[character] {
                closers.append(closer)
            } else if character == closers.last {
                closers.removeLast()
            } else {
                return false
            }
        }
        
        return closers.isEmpty
        
        //시간 O(n) (string의 길이)
        //공간 O(n)
    }
}

