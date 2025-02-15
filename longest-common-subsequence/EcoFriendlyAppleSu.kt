package leetcode_study

/*
* 가장 긴 공통 부분 문자열의 길이를 구하는 문제
* 동적 계획법을 사용한 문제 해결
* 문자가 동일할 경우, table[i][j] = table[i-1][j-1] + 1. 즉, 이전까지의 최장 공통 부분 문자열 길이에 1을 추가
* 문자가 다를 경우, table[i][j] = max(table[i-1][j], table[i][j-1]) 이는 현재까지 찾은 최장 공통 부분 문자열의 길이를 유지하는 과정
*
* 시간 복잡도: O(n^2)
* -> 두 분자열을 이중 반복을 진행하는 경우
* 공간 복잡도: O(nm) (= n과 m은 각각 주어진 문자열을 길이)
* -> dp table에 사용되는 공간
* */
fun longestCommonSubsequence(text1: String, text2: String): Int {
    val n = text1.length
    val m = text2.length
    val dp = Array(n + 1) { IntArray(m + 1) }

    for (i in 1..n) {
        for (j in 1..m) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = maxOf(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[n][m]
}

/*
* 주어진 두 문자열에 각각의 Index를 두어 비교해가며 해결 시도 해당 방법으로 시도
* Test case를 통과했지만 "bac", "abc"와 같은 case에서 "bc"를 답으로 도출할 수 있지만 "ac"와 같은 경우는 지나치게됨
* 즉, 정답이 되는 경우를 제외할 수 있음.
* */
fun longestCommonSubsequence(text1: String, text2: String): Int {
    var result = 0
    var longOne: String
    var shortOne: String
    var longIndex = 0
    var shortIndex = 0

    if (text1.length >= text2.length) {
        longOne = text1
        shortOne = text2
    } else {
        longOne = text2
        shortOne = text1
    }

    while (shortIndex < shortOne.length) {
        if (shortOne[shortIndex] == longOne[longIndex]) {
            shortIndex += 1
            longIndex += 1
            result += 1
        } else {
            longIndex += 1
        }
        if (longIndex == longOne.length) break
    }

    return result
}
