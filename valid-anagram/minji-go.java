/*
    Problem: https://leetcode.com/problems/valid-anagram/
    Description: return true if one string is an anagram of the other, one formed by rearranging the letters of the other
    Concept:String, Hash Table, Sorting, Array, Counting, String Matching, Ordered Map, Ordered Set, Hash Function ...
    Time Complexity: O(n), Runtime: 27ms
    Space Complexity: O(n), Memory: 43.11MB
*/
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map<Character, Integer> count = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0)+1);
            count.put(t.charAt(i), count.getOrDefault(t.charAt(i), 0)-1);
        }
        for(Character key : count.keySet()){
            if(count.get(key)!=0) return false;
        }
        return true;
    }
}
