// TC: O(n)
// using two pointer lef and right, it visits all elements only once each.
// SC: O(n + m)
// 2 hashmap used for checking the given Strings s and t, n is the size of s, m is the size of m
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();

        for (char c : t.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int required = map.size();
        int formed = 0;

        int left = 0;
        int right = 0;
        int[] ans = {-1, 0, 0};

        Map<Character, Integer> windowCounts = new HashMap<>();

        while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);

            if (map.containsKey(c) &&
                    windowCounts.get(c).intValue() == map.get(c).intValue()) {
                formed += 1;
            }

            while (left <= right && formed == required) {
                c = s.charAt(left);

                if (ans[0] == -1 || right - left + 1 < ans[0]) {
                    ans[0] = right - left + 1;
                    ans[1] = left;
                    ans[2] = right;
                }

                windowCounts.put(c, windowCounts.get(c) - 1);
                if (map.containsKey(c) &&
                        windowCounts.get(c).intValue() < map.get(c).intValue()) {
                    formed -= 1;
                }

                left += 1;
            }
            right += 1;
        }
        return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }
}
