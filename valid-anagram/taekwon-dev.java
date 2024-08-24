/**
 * 처음 문제를 보고 들었던 생각: 정렬 시켜서 같으면 anagram?
 * 근데, 정렬 시켜서 같다면, 결국 문자열을 구성하는 각 문자의 빈도수가 같다.
 *
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(1)
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] charCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            int index = t.charAt(i) - 'a';
            charCount[index]--;
            if (charCount[index] < 0) {
                return false;
            }
        }

        return true;
    }
}
