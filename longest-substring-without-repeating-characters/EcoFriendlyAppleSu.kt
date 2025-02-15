package leetcode_study

/*
* 주어진 문자열에서 반복되는 문자를 포함하지 않은 가장 긴 부분 문자열의 길이를 구하는 문제
* 이중 반복문을 사용해 바깥 반복문에선 시작 문자를 내부 반복문에선 그 다음 문자를 순회하며 중복된 문자가 발견되었을 때, 반복문 탈출하는 방법으로 문제 해결
* 시간 복잡도: O(n^2)
* -> 이중 반복 과정
* 공간 복잡도: O(n)
* -> 중복되지 않은 문자열을 담을 공간 필요
* */
fun lengthOfLongestSubstring(s: String): Int {
    var maximumLength = 0
    for (start in s.indices) {
        val tempList = mutableListOf<Char>()
        for (end in start until s.length) {
            if (tempList.contains(s[end])) {
                break // escape loop
            }
            tempList.add(s[end])
            maximumLength = max(tempList.size, maximumLength)
        }
    }
    return maximumLength
}
