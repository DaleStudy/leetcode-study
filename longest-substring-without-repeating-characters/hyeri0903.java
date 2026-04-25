class Solution {
    public int lengthOfLongestSubstring(String s) {
        /**
        1.prob: 중복없는 가장 긴 substring length return
        2.constraints:
        - alphabet, digit, space 로 구성
        - s.length min = 0, max = 50,000
        3.solution
        - slding window, time: O(n), space: O(n) or O(1)
         */

         int maxLen = 0;
         int left = 0;
         Set<Character> visited = new HashSet<>();

         for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            while(visited.contains(ch)) {
                visited.remove(s.charAt(left));
                left += 1;
            }
            visited.add(ch);
            maxLen = Math.max(maxLen, i - left + 1);
         }
    
        return maxLen;
    }
}
