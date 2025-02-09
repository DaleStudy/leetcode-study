// DP라 생각하고 시간을 너무 많이써서 GPT에게 물어보니 아예 접근 자체를 잘못함
// 다시 생각해봐야할듯
class Solution {
    public String minWindow(String s, String t) {
        if (s == null || s.length() == 0 || t == null || t.length() == 0) return "";

        // 1️⃣ t의 문자 개수를 카운트해서 저장
        Map<Character, Integer> tCount = new HashMap<>();
        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }
        int required = tCount.size(); // 필요한 고유 문자 개수

        // 2️⃣ 슬라이딩 윈도우 변수 초기화
        int left = 0, right = 0; // 윈도우 포인터
        int formed = 0; // t의 문자 개수를 만족하는 개수
        Map<Character, Integer> windowCounts = new HashMap<>();

        int minLength = Integer.MAX_VALUE;
        int startIdx = 0;

        // 3️⃣ 슬라이딩 윈도우 확장
        while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);

            if (tCount.containsKey(c) && windowCounts.get(c).intValue() == tCount.get(c).intValue()) {
                formed++;
            }

            // 4️⃣ 모든 문자가 포함되었을 때, 윈도우 크기를 줄이면서 최소 길이 찾기
            while (left <= right && formed == required) {
                char leftChar = s.charAt(left);

                // 최소 길이 갱신
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    startIdx = left;
                }

                // 윈도우 크기를 줄이기 위해 left 이동
                windowCounts.put(leftChar, windowCounts.get(leftChar) - 1);
                if (tCount.containsKey(leftChar) && windowCounts.get(leftChar) < tCount.get(leftChar)) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        // 5️⃣ 결과 반환
        return (minLength == Integer.MAX_VALUE) ? "" : s.substring(startIdx, startIdx + minLength);
    }
}
