package leetcode_study

/**
 * 시간복잡도 : O(n) ?
 * -
 * 공간복잡도 : O(n)
 * - charAndIdx 에 최대 n개의 문자에 대해서 담을 수 있으므로 O(n) 의 공간복잡도를 가집니다.
 * */

fun lengthOfLongestSubstring(s: String): Int {
    var point = 0
    val charAndIdx = HashMap<Char, Int>()
    var cnt = 0
    var maxCnt = 0

    while (point < s.length) {
        val nowChar = s[point]
        if (nowChar !in charAndIdx.keys) {
            charAndIdx[nowChar] = point
            cnt += 1
            point += 1
        } else {
            val prevSameCharIdx = charAndIdx[nowChar]!!
            point = prevSameCharIdx + 1
            charAndIdx.clear()
            cnt = 0
        }

        maxCnt = maxOf(cnt, maxCnt)
    }

    return maxCnt
}
