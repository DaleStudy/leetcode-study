// 최근 자주 보였던 슬라이딩 윈도우를 이용한 방법 
// 시간 복잡도 : O(N)
class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0, maxLen = 0;
        int[] count = new int[26];
        int maxCount = 0;

        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++; // 오른쪽 문자 추가
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']); // 최빈 문자 업데이트

            // 현재 윈도우의 크기 - 최빈 문자 개수 > k라면 윈도우를 축소
            while ((right - left + 1) - maxCount > k) {
                count[s.charAt(left) - 'A']--; // 왼쪽 문자 제거
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);  // 최대 길이 업데이트
        }

        return maxLen;
    }
}
