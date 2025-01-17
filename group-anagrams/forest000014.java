/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            int[] cnt = new int[26];
            for (int i = 0; i < str.length(); i++) {
                cnt[str.charAt(i) - 'a']++;
            }
            char[] chars = new char[str.length()];
            int idx = 0;
            for (int i = 0; i < 26; i++) {
                while (cnt[i] > 0) {
                    chars[idx++] = (char)(i + 'a');
                    cnt[i]--;
                }
            }
            String sorted = new String(chars);
            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>());
            }
            map.get(sorted).add(str);
        }

        List<List<String>> ans = new ArrayList<>();
        for (String key : map.keySet()) {
            ans.add(new ArrayList<>());
            for (String str : map.get(key)) {
                ans.get(ans.size() - 1).add(str);
            }
        }

        return ans;
    }
}
