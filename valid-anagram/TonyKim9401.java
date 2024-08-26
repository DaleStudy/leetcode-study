class Solution {
    public boolean isAnagram(String s, String t) {
        // time complexity: O(n log n)
        // space complexity: O(n)
        if (s.length() != t.length()) return false;

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        Arrays.sort(sArr);
        Arrays.sort(tArr);

        return Arrays.equals(sArr, tArr);
    }
}
