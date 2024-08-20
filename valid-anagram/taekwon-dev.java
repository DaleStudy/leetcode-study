/**
 * 시간 복잡도: O(NlogN)
 *   - Arrays.sort() > Dual-Pivot QuickSort
 *
 * 공간 복잡도: O(N)
 *
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}
