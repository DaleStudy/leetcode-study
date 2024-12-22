/*
    Problem: https://leetcode.com/problems/valid-anagram/
    Description: return true if one string is an anagram of the other, one formed by rearranging the letters of the other
    Concept:String, Hash Table, Sorting, Array, Counting, String Matching, Ordered Map, Ordered Set, Hash Function ...
    Time Complexity: O(n), Runtime: 27ms
    Space Complexity: O(n), Memory: 43.05MB
*/
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map<Character, Integer> charCount = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            charCount.put(s.charAt(i), charCount.getOrDefault(s.charAt(i), 0)+1);
            charCount.put(t.charAt(i), charCount.getOrDefault(t.charAt(i), 0)-1);
        }
        for(Integer count : charCount.values()){
            if(count !=0) return false;
        }
        return true;
    }
}
