/**
 * TC : O(n)
 *  - 문자열 길이 n 만큼 순회하므로 O(n)
 * SC : O(min(m, n))
 *   - map 의 최대 크기는 문자열 길이 n과 알파벳 종류 수 m == 26 중 더 작은 수이므로 O(min(m, n))
 */
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // "abcabcbb"
        //  v  - cursor = maxLen;
        int maxLen = 0;
        Map<Character, Integer> map = new HashMap<>();

        int anchor = 0;
        for(int cursor = 0; cursor < s.length(); cursor++) {
            char c = s.charAt(cursor);
            
            if(map.containsKey(c)) {
                anchor = Math.max(anchor, map.get(c) + 1);
            }

            map.put(c, cursor);

            maxLen = Math.max(maxLen, cursor - anchor + 1);
        }
        return maxLen;
    }
}
