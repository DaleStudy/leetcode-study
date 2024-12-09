package leetcode_study

/**
 * 문자열의 대칭 판단
 * 시간 복잡도 : O(n)
 * -> 주어진(n) 크기의 문자열을 순회하며 비교함
 */
fun isPalindrome(s: String): Boolean {

    // 주어진 문자열에서 모든 non-alphanumeric characters를 필터한 문자 배열 할당
    val splitGivenString = s.toCharArray()
        .filter { it.isLetterOrDigit() }
        .map { it.lowercaseChar() }
        .toCharArray()

    // 필터된 문자열이 비어있다면 true 반환
    if (splitGivenString.isEmpty()) { return true }

    // 대칭을 비교하기 위한 시작, 끝 변수
    var start = 0
    var end = splitGivenString.size - 1

    // 반복적으로 수행하며 같다면 시작 +1, 끝 -1 을 진행해 대칭 판단
    while (start <= end) {
        if (splitGivenString[start] == splitGivenString[end]) {
            start += 1
            end -= 1
            continue
        }
        return false
    }
    return true
}
