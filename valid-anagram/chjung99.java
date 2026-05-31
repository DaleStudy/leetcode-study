/**
 * time: O(n)
 * space: O(1)
 */

class Solution {
    public boolean isAnagram(String s, String t) {
        int[] countS = new int[26];
        int slen = s.length();
        int tlen = t.length();

        if (slen != tlen) return false;

        for (int i = 0; i < slen; i++){
            countS[s.charAt(i)-'a'] += 1;
            countS[t.charAt(i)-'a'] -= 1;
        }
        for (int i = 0; i < 26; i++){
            if (countS[i] != 0) return false;
        }
        return true;
    }
}

