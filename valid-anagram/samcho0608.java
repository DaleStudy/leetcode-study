import java.util.HashMap;

// link: https://leetcode.com/problems/valid-anagram/
// difficulty: Easy
class Solution1 {
    // Problem:
    // * return: is t an anagram of s
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int n = s.length();

        // Space Complexity: O(N)
        HashMap<Character, Integer> freqS = new HashMap<>();
        HashMap<Character, Integer> freqT = new HashMap<>();

        // Time Complexity: O(N)
        for(int i = 0; i < n; i++) {
            char charS = s.charAt(i);
            freqS.put(charS, freqS.getOrDefault(charS, 0) + 1);

            char charT = t.charAt(i);
            freqT.put(charT, freqT.getOrDefault(charT, 0) + 1);
        }

        // Time Complexity: O(N)
        for(var entryS: freqS.entrySet()) {
            int cntT = freqT.getOrDefault(entryS.getKey(), 0);
            if(cntT != entryS.getValue()) return false;
        }

        return true;
    }
}

// Map 하나만 사용하는 개선된 방식
class Solution2 {
    // Problem:
    // * return: is t an anagram of s
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int n = s.length();

        // Space Complexity: O(N)
        HashMap<Character, Integer> freq = new HashMap<>();

        // Time Complexity: O(N)
        for(int i = 0; i < n; i++) {
            char charS = s.charAt(i);
            freq.put(charS, freq.getOrDefault(charS, 0) + 1);

            char charT = t.charAt(i);
            freq.put(charT, freq.getOrDefault(charT, 0) - 1);
        }

        // Time Complexity: O(N)
        for(int count: freq.values()) {
            if(count != 0) return false;
        }

        return true;
    }
}