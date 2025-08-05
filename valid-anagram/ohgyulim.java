class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N)
    * 
    * 공간 복잡도: O(52)
    */ 
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] sCounts = new int[26];
        int[] tCounts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sCounts[s.charAt(i) - 'a'] += 1;
            tCounts[t.charAt(i) - 'a'] += 1;
        }

        for (int i = 0; i < 26; i++) {
            if (sCounts[i] != tCounts[i]) return false;
        }

        return true;
    }
}
