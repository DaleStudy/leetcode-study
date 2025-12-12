/**
 * Runtime: 2ms
 * Time Complexity: O(n)
 *
 * Memory: 44.56MB
 * Space Complexity: O(1)
 *
 * Approach: a~z 알파벳 개수 배열을 사용하여 짝을 이루는지 검사
 * - 알파벳 개수가 똑같다면 +- 했을 때 0이 됨
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] checkedArr = new int[26];
        for (char element: s.toCharArray()) {
            int index = (int)element - 'a';
            checkedArr[index]++;
        }

        for (char element: t.toCharArray()) {
            int index = (int)element - 'a';
            checkedArr[index]--;
        }

        for (int alphabet: checkedArr) {
            if (alphabet != 0)
                return false;
        }

        return true;
    }
}
