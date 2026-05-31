class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        // 애너그램을 저장할 딕셔너리
        var groups = [String: [String]]()
        
        for str in strs {
            // 각각의 문자열별로 등장하는 글자의 갯수를 저장할 딕셔너리
            var occurences = [Character: Int]()

            // 등장하는 글자의 갯수를 계산
            // Swift에서는 글자를 다루기 위해 배열로 변환하는 것이 좋음
            for letter in Array(str) {
                if let val = occurences[letter] {
                    occurences[letter] = val + 1
                } else {
                    occurences[letter] = 1
                }
            }

            let anagramKey = makeAnagramKey(for: occurences)
            
            // 딕셔너리에 이미 같은 애너그램 키가 존재할 경우, 해당 키에 대한 값에 현재 문자열 추가
            if let group = groups[anagramKey] {
                groups[anagramKey]!.append(str)
            } else {
                // 딕셔너리에 키가 존재하지 않을 경우, 키를 추가하고 현재 문자열을 값으로 추가
                groups[anagramKey] = [str]
            }
        }

        // 딕셔너리의 값들을 배열로 반환 - 반환 순서는 상관없다고 문제에 명시
        // 반환 순서가 필요할 경우 애너그램 키의 등장 순서를 저장하는 딕셔너리를 새로 만들 수 있음
        return Array(groups.values)
    }

    // 등장하는 글자의 갯수에 따라 딕셔너리의 키를 만드는 함수
    func makeAnagramKey(for occurences: [Character: Int]) -> String {
        // 같은 애너그램을 가질 때 같은 키를 반환하게 하기 위해, 정렬 적용
        return occurences.keys.sorted().reduce("") { (previous, key) in 
            var previous = previous
            previous += String(key)
            previous += String(occurences[key]!)
            
            return previous
        }
    }
}
