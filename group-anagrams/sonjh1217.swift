class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var stringsByCount = [[Int]: [String]]()
        
        strs.map { str in
            var countsByAlphabet = Array(repeating: 0, count: 26)
            for char in str.unicodeScalars {
                countsByAlphabet[Int(char.value) - 97] += 1
            }
            stringsByCount[countsByAlphabet, default: []].append(str)
        }
        
        return Array(stringsByCount.values)
    }
    //시간 O(n*L) L=string들의 평균 길이
    //공간 O(n*L)
}

