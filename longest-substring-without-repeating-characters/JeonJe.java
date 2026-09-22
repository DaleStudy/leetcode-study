import java.util.*;

// TC: O(n)
// SC: O(min(n, m)) (m = 문자 집합 크기)
class Solution {
    public int lengthOfLongestSubstring(String s) {

        int answer = 0;
        int left = 0;

        Set<Character> temp = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {

            // 중복이 사라질 때까지 s[left]를 set에서 빼며 left를 전진시킨다.
            while (temp.contains(s.charAt(right))) {
                temp.remove(s.charAt(left));
                left++;
            }

            temp.add(s.charAt(right));
            answer = Math.max(answer, right - left + 1);
        }

        return answer;
    }
}
