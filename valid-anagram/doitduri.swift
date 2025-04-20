class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        guard s.count == t.count else { 
            return false
        }

        return s.sorted() == t.sorted()
    }
}
