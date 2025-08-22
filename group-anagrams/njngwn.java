// Time Complexity: O(n), n: strs.length
// Space Complexity: O(m+n), m: strMap.size, n: anagramList.size
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> strMap = new HashMap<String, ArrayList<String>>();

        for (String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String key = String.valueOf(charArr);

            if (strMap.containsKey(key)) {
                strMap.get(key).add(str);
            } else {
                strMap.put(key, new ArrayList<String>(Arrays.asList(str)));
            }
        }

        return new ArrayList<>(strMap.values());
    }
}
