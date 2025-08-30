class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let filtered = s.filter {$0.isLetter || $0.isWholeNumber}.lowercased()
        let reversed = String(filtered.reversed())
        
        return filtered == reversed
        
        //시간 복잡도 O(n)
        //공간 복잡도 O(n)
    }
}

