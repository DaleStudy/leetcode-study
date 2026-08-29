class Solution {
    public int characterReplacement(String s, int k) {
        int[] frequency = new int[26];
        int maxFrequency = 0;
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            int index = s.charAt(right) - 'A';
            frequency[index]++;

            // maxFrequency 갱신
            maxFrequency = Math.max(maxFrequency, frequency[index]);

            // right - left + 1 - maxFrequency : 현재 위도우에서 maxFrequency를 제외한 개수
            while (right - left + 1 - maxFrequency > k) {
                frequency[s.charAt(left) - 'A']--;
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}
