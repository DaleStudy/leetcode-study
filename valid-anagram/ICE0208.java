import java.util.Arrays;

class Solution {
    /**
     * n = s.length(), m = t.length()
     * 각 문자열에서 알파벳별 등장 횟수를 센 뒤 비교한다.
     * 시간 복잡도: O(n + m)
     * 공간 복잡도: O(1) - 알파벳 소문자 26개만 사용하기 때문
     */
    public boolean isAnagram(String s, String t) {
        // 0: a, 1: b, ... , 25: z
        int[] sCount = new int[26];
        int[] tCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            tCount[t.charAt(i) - 'a']++;
        }

        return Arrays.equals(sCount, tCount);
    }
}
