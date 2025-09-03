class Solution {
    // O(n) time / O(n) space
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var lastIndexByCharacter = [Character: Int]()
        var start = 0
        var maxLenth = 0

        for (i, character) in s.enumerated() {
            if let lastIndex = lastIndexByCharacter[character],
                lastIndex >= start {
                start = lastIndex + 1
            }
            lastIndexByCharacter[character] = i
            maxLenth = max(maxLenth, i - start + 1)
        }
        return maxLenth
    }
}

