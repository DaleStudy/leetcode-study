// time : O(n)
// space : O(1)

class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) return false;
        
        int[] charCount = new int[26];

        for(int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
            charCount[t.charAt(i) - 'a']--;
        }

        for(int i : charCount) {
            if(i != 0) {
                return false;
            }
        }
        
        return true;
    }
}
