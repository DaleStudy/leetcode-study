/**
 * https://leetcode.com/problems/group-anagrams/
 *
 * time: O(n * m log m)
 * space: O(nm)
 */
class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap();
        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            groups.computeIfAbsent(new String(arr), k -> new ArrayList<>())
                  .add(str);
        }
        return new ArrayList(groups.values());
    }
}
