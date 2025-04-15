class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool { // O(n)
        // s 문자열의 문자를 키로 빈도수를 값으로 저장
        var baseDict = Dictionary(s.map{($0,1)}, uniquingKeysWith: +)
        
        for char in t { // t를 반복하면서 존재하는지 확인, 만약 없다면 return false
            guard baseDict[char] != nil, baseDict[char] != 0
            else { return false }

            baseDict[char]? -= 1
            if baseDict[char] == 0 {
                baseDict.removeValue(forKey: char)
            }
        }
        return baseDict.isEmpty
    }
}

// MARK: 가장 간단한 방법 time: O(nlogn)
class Solution2 {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        s.sorted() == t.sorted()
    }
}

// MARK: 실행속도가 가장 빠름 time: O(n)
class Solution3 {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        guard s.count == t.count else { return false }

        let sCharCount = getCharacterCount(s)
        let tCharCount = getCharacterCount(t)
        // 반환된 배열이 동일하면 애너그램
        return sCharCount == tCharCount
    }
    // 배열로 문자 빈도수를 처리 및 저장
    private func getCharacterCount(_ str: String) -> [Int] {
        var charCount = [Int](repeating: 0, count: 26)
        let aAsciiValue = Character("a").asciiValue ?? 0

        for char in str.utf8 {
            charCount[Int(char - aAsciiValue)] += 1
        }

        return charCount
    }
}
