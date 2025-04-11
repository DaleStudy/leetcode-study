//문자열 s, t를 받고, t가 s의 애너그램이면 true, 아니면 false 출력

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        ///둘이 문자 갯수가 다르다면 바로 False
        if s.count != t.count { return false }
        
        ///해쉬테이블 사용
        var wordDic: [Character: Int] = [:]

        ///s의 글자들은 1씩 추가, t의 글자들은 1씩 감소
        for (sChar, tChar) in zip(s, t) {
            wordDic[sChar, default: 0] += 1
            wordDic[tChar, default: 0] -= 1
        }

        ///딕셔너리의 모든 값이 상쇄되어 0이 되면 true
        return wordDic.values.allSatisfy { $0 == 0 }
    }
}
