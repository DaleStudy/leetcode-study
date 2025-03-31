class Solution {
    fun minWindow(s: String, t: String): String {
        if (s.length < t.length) {
            return ""
        }
        val containIndexList = mutableListOf<Int>()
        for (i in s.indices) {
            if (t.contains(s[i])) {
                containIndexList.add(i)
            }
        }
        var answer = ""
        val regex =
            t.toCharArray().joinToString(separator = "", prefix = "^", postfix = ".+$") { """(?=.*${it})""" }.toRegex()
        for (i in 0..containIndexList.size - t.length) {
            val startIndex = containIndexList[i]
            for (l in t.length..containIndexList.size - i) {
                val endIndex = containIndexList[(i + l) - 1] + 1
                val subStr = s.substring(startIndex, endIndex)
                if (regex.containsMatchIn(subStr)) {
                    if (answer.isEmpty()) {
                        answer = subStr
                    } else if (subStr.length < answer.length) {
                        answer = subStr
                    }
                    break
                }
            }
        }
        return answer
    }
}
