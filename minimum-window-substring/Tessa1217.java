import java.util.HashMap;
import java.util.Map;

class Solution {

    // 시간복잡도: O(n), 공간복잡도 O(1)
    public String minWindow(String s, String t) {

        int strLength = s.length();
        int targetLength = t.length();

        // 목표 분자열이 주어진 문자열보다 길다면 부분 문자열로 볼 수 없음
        if (targetLength > strLength) {
            return "";
        }

        // 목표 문자열에 필요한 문자와 그 개수를 담는 맵
        Map<Character, Integer> charMap = new HashMap<>();

        for (char c : t.toCharArray()) {
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }

        // 투 포인터 선언
        int left = 0;
        int right = 0;
        int minWindowLength = Integer.MAX_VALUE;
        int minWindowStart = 0; // 최소 윈도우 시작 위치  
        int remaining = targetLength;

        while (right < strLength) {

            Character end = s.charAt(right);

            if (charMap.containsKey(end)) {
                charMap.put(end, charMap.get(end) - 1);
                if (charMap.get(end) >= 0) {
                    remaining--;
                }
            }

            // target 문자열의 모든 문자를 찾았다면 left 포인터 이동하면서
            // 최소 윈도우 찾기 시작
            while (remaining == 0) {
                if (right - left + 1 < minWindowLength) {
                    minWindowLength = right - left + 1;
                    minWindowStart = left;
                }

                char startChar = s.charAt(left);
                if (charMap.containsKey(startChar)) {
                    charMap.put(startChar, charMap.get(startChar) + 1);
                    if (charMap.get(startChar) > 0) {
                        remaining++;
                    }
                }

                left++;
            }

            right++;

        }

        return minWindowLength == Integer.MAX_VALUE ? ""
                : s.substring(minWindowStart, minWindowStart + minWindowLength);

    }
}

