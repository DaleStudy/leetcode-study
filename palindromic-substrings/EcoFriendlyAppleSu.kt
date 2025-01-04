package leetcode_study

/*
* 주어진 문자열에서 자른 개별 문자열이 회문일 경우를 판단하는 문제
* 시간 복잡도: O(n^3)
* -> 주어진 문자열을 자를 때 이중 반복문 수행: O(n^2)
* -> subString() 함수는 내부적으로 주어진 k 만큼 복사된 문자열 객체를 만들기 때문에 O(n) 소요
* --> O(n) * O(n^2) = O(n^3)
* 공간 복잡도: O(n)
* -> subString() 함수가 호출될 때마다 길이 k의 새로운 문자열 객체가 생성되기 때문에 subString 최대 길이인 O(n)을 가짐.
* */
fun countSubstrings(s: String): Int {
    var count = 0

    val maxLength = s.length
    for (startIndex in 0 until maxLength) {
        for (endIndex in startIndex + 1..maxLength) {
            val temp = s.substring(startIndex, endIndex)
            if (temp == temp.reversed()) {
                count++
            }
        }
    }
    return count
}

/*
* 자른 문자열을 개별적으로 회문인지 판단해야하는데 주어진 문자열에서 포함하는 것으로 문제를 해석하고
* 해결했기 때문에 통과하지 못함
* */
fun countSubstrings01(s: String): Int {
    val result = mutableListOf<String>()
    val maxLength = s.length
    var startIndex = 0
    while (startIndex < maxLength) {
        val endIndex = startIndex + 1
        for (i in endIndex until maxLength + 1) {
            val temp = s.substring(startIndex, i)
            if (s.contains(temp.reversed())) {
                result.add(temp)
            }
        }
        startIndex += 1
    }
    return result.size
}
