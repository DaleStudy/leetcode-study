class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        var wordArray = Array(repeating: false, count: s.count + 1)
        wordArray[0] = true
        for i in 1...s.count {
            for j in 0..<i {
                if wordArray[j] {
                    let startIndex = s.index(s.startIndex, offsetBy: j)
                    let endIndex = s.index(s.startIndex, offsetBy: i)
                    let word = String(s[startIndex..<endIndex])
                    if wordDict.contains(word) {
                        wordArray[i] = true
                    }
                }
            }
        }
        return wordArray[s.count]
    }
}
 
