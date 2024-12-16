class Solution {
    
    /*
        Runtime: 16 ms (Beats 84.96%)
        Time Complexity: O(n)
            - 길이가 n인 str s, str t, dict counter를 순회하므로 O(3n) ~= O(n)
        Space Complexity: O(n)
            - 크기가 최대 n인 dict를 변수로 저장하여 사용하므로 O(n)
        Memory: 16.01 MB (Beats 97.18%)
    */
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var countDict: [String.Element: Int] = [:]
        
        for char in s {
            countDict[char] = (countDict[char] ?? 0) + 1
        }
        
        for char in t {
            guard let count = countDict[char] else {
                return false
            }
            
            countDict[char] = count - 1
        }
        
        for count in countDict.values {
            if count != 0 {
                return false
            }
        }
        
        return true
    }
}
