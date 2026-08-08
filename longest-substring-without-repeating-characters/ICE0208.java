import java.util.Arrays;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int [] lastSeen = new int[128];
        Arrays.fill(lastSeen, -1);

        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);

            // 현재 문자가 이미 등장했다면
            // 이전 등장 위치 다음으로 left를 이동한다.
            // left는 right 보다 작거나 같다는 것이 보장.
            left = Math.max(left, lastSeen[current] + 1);

            lastSeen[current] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
