import java.util.Arrays;

// tag renovizee 2week
// https://github.com/DaleStudy/leetcode-study/issues/218
// https://leetcode.com/problems/valid-anagram/ #242 #Easy
class Solution {
    // Solv1
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
    public boolean isAnagram(String s, String t) {

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}

//-------------------------------------------------------------------------------------------------------------
// Java 문법 피드백
// 1) string.toCharArray
// 2) Arrays.~ 문법 ~.sort ~.equals
// 3) Arrays.
//-------------------------------------------------------------------------------------------------------------
