/*
 시간복잡도 : O(N)
 공간복잡도 : O(1)
 */

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] character = new int[26];

        for(int i = 0; i < s.length(); i++) {
            character[s.charAt(i) - 'a']++;
            character[t.charAt(i) - 'a']--;
        }


        for(int num : character) {
            if(num != 0)
                return false;
        }

        return true;

    }
}
