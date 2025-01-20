class Solution {
    // 시간 : O(n) 공간 : O(n)
    fun lengthOfLongestSubstring(s: String): Int {
        var max = 0
        val subStr = StringBuffer()
        s.forEach {     // s를 조회하면서 글자를 subStr에 담는다.
            if (subStr.contains(it)) {     // 단, 겹치는 글자가 있을경우 subStr의 len을 기록하고, 초기화 한다.
                max = max(max, subStr.length)
                subStr.delete(0, subStr.length)
            }
            subStr.append(it)
        }
        max = max(max, subStr.length)
        println(subStr)
        return max
    }
}
