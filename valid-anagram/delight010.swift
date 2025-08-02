class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var sDictionary: [Character: Int] = [:]
        var tDictionary: [Character: Int] = [:]
        for char in s {
            sDictionary[char] = (sDictionary[char] ?? 0) + 1
        }
        for char in t {
            tDictionary[char] = (tDictionary[char] ?? 0) + 1
        }
        return sDictionary == tDictionary
    }
}
 
