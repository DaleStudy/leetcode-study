import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        // TC = O(n)
        // SC = O(n)
        HashMap<Character, Integer> sMap = new HashMap<>();

        for (char c : s.toCharArray()) {
            sMap.merge(c, 1, Integer::sum);
        }

        for (char c : t.toCharArray()) {
            if (sMap.getOrDefault(c, 0) == 0) {
                return false;
            }
            sMap.merge(c, -1, Integer::sum);
        }

        return true;
    }
}
