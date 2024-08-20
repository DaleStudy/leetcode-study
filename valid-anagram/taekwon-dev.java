/**
 * 시간 복잡도: O(NlogN)
 *   - Arrays.sort() > Dual-Pivot QuickSort
 *
 * 공간 복잡도: O(N)
 *
 * 처음 문제를 보고 들었던 생각: 정렬 시켜서 같으면 anagram?
 * -> 아, 그러면 등장한 문자의 빈도수가 같네?
 * -> 결국 26 사이즈가 인풋에 영향을 받지 않으므로 공간 복잡도를 O(1)로 개선할 수 있고,
 * -> 시간 복잡도도 O(N)으로 개선할 수 있겠다.
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] charCount = new int[26];

        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            charCount[c - 'a']--;
            if (charCount[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}
