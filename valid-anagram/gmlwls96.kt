class Solution {
    // 시간 복잡도 : O(nlog(n))
    fun isAnagram(s: String, t: String): Boolean {
        val sortS = s.toCharArray().apply { sort() } // string을 char array로 변환 후 정렬.
        val sortT = t.toCharArray().apply { sort() }
        return sortS.concatToString() == sortT.concatToString() // 정렬된 char array를 string으로 만든후 비교.
    }
}
