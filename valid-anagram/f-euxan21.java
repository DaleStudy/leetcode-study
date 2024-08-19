// time : O(n)
// space : O(n)

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sToChar = s.toCharArray();
        char[] tToChar = t.toCharArray();
        
        int[] charCount = new int[26];

        for(char c : sToChar) {
            charCount[c - 'a']++;
        }

        for(char c : tToChar) {
            charCount[c - 'a']--;
        }

        for(int i : charCount) {
            if(i != 0) {
                return false;
            }
        }
        
        return true;
    }
}
