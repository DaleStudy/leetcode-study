// TC: O(n)
// SC: O(n * m)
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            String target = new String(charArray);

            if (map.containsKey(target)) {
                map.get(target).add(strs[i]);
            } else {
                List<String> inside = new ArrayList<>();
                inside.add(strs[i]);
                map.put(target, inside);
            }
        }

        for (String key : map.keySet()) output.add(map.get(key));
        return output;
    }
}
