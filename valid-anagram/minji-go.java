/**
 * <a href="https://leetcode.com/problems/valid-anagram/">week02-1.valid-anagram</a>
 * <li> Description: return true if one string is an anagram of the other, one formed by rearranging the letters of the other   </li>
 * <li> Concept:String, Hash Table, Sorting, Array, Counting, String Matching, Ordered Map, Ordered Set, Hash Function ...      </li>
 * <li> Time Complexity: O(n), Runtime: 15ms    </li>
 * <li> Space Complexity: O(n), Memory: 44.66MB </li>
 */

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Integer, Integer> tmap = t.chars()
                .boxed()
                .collect(Collectors.toMap(i -> i, i -> 1, (i1, i2) -> i1 + i2));

        Map<Integer, Integer> smap = s.chars()
                .boxed()
                .collect(Collectors.toMap(i -> i, i -> 1, (i1, i2) -> i1 + i2));

        return tmap.equals(smap);
    }
}