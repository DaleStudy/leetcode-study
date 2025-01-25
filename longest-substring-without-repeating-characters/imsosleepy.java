// 각 문자를 한번씩 처리하도록 슬라이딩 윈도우 방식을 채택
// 시간복잡도 : O(n) - 각 문자를 한 번씩 처리
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        int startIdx = 0;
        String currentSubstring = "";

        for (int i = 0; i < s.length(); i++) {
            int duplicateIdx = currentSubstring.indexOf(s.charAt(i));
            
            // 중복 문자가 발견되면 윈도우의 시작 위치를 조정
            if (duplicateIdx != -1) {
                startIdx = startIdx + duplicateIdx + 1;
            }

            currentSubstring = s.substring(startIdx, i + 1);
            maxLength = Math.max(maxLength, currentSubstring.length());
        }

        return maxLength;
    }
}
