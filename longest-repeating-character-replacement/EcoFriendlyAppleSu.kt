package leetcode_study

/*
* 문제를 해결에 @Dale 님의 설명 참고. Sliding Window 기법을 통해 문자열 처리
* 시간 복잡도: O(n)
* -> 주어진 문자열을 순회하면서 문자열 처리: O(n)
* -> 문자의 빈도 갱신 연산: O(1)
*
* 공간 복잡도: O(1)
* -> 문자의 개수를 저장하는데 Map 자료구조 사용. 최대 26개의 대문자 저장 공간 필요: O(1)
* */
fun characterReplacement(s: String, k: Int): Int {
    var maxLen = 0
    val counter = mutableMapOf<Char, Int>()
    var start = 0

    for (end in s.indices) {
        counter[s[end]] = counter.getOrDefault(s[end], 0) + 1 // character mapping

        // 부분 문자열의 길이에서 가장 많이 들어있는 글자의 수를 뺀 값이 k보다 클 경우 시작(start) 포인터를 이동
        // k 만큼 변경했을 때, 연속할 수 있는 문자를 만들 수 있도록 조정
        while (end - start + 1 - (counter.values.maxOrNull() ?: 0) > k) {
            counter[s[start]] = counter.getOrDefault(s[start], 0) - 1
            start++
        }

        // 탐색한 부분 문자열 중 가장 긴 문자열의 값을 저장
        maxLen = maxOf(maxLen, end - start + 1)
    }
    return maxLen
}
