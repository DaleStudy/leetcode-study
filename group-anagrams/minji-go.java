/**
 * <a href="https://leetcode.com/problems/group-anagrams/">week05-2.group-anagrams</a>
 * <li>Description: Given an array of strings strs, group the anagrams together</li>
 * <li>Topics: Array, Hash Table, String, Sorting</li>
 * <li>Time Complexity: O(N*KLogK), Runtime 6ms  </li>
 * <li>Space Complexity: O(N*K), Memory 47.82MB  </li>
 */
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mapOfAnagrams = new HashMap<>();

        for(String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            List<String> anagrams = mapOfAnagrams.computeIfAbsent(key, k -> new ArrayList<>());
            anagrams.add(str);
        }

        return new ArrayList<>(mapOfAnagrams.values());
    }
}
