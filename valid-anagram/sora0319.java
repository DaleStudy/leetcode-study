class Solution {
    public boolean isAnagram(String s, String t) {
        int[] character = new int[26];
        if(s.length() != t.length()) return false;

        for(int i = 0; i < t.length(); i++){
            int place = t.charAt(i) - 'a';
            character[place]++;
        }

        for(int i = 0; i < s.length(); i++){
            int place = s.charAt(i) - 'a';
            if(character[place] <= 0) return false;
            character[place]--;
        }
        return true;
    }
}


