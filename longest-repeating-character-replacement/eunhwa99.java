class Solution{
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0;
        int left = 0;
        int result = 0;

        for (int right = 0; right < s.length(); right++) { // sliding window에서의 right pointer
            char currentChar = s.charAt(right);
            count[currentChar - 'A']++; // 현재 문자 카운트 증가
            maxCount = Math.max(maxCount, count[currentChar - 'A']);

            while (right - left + 1 - maxCount > k) { // 현재 window의 길이 - 가장 많이 등장한 문자 개수 > k
                 // 윈도우 크기 - maxCount > k가 되면, k번의 변경으로는 모든 문자를 동일하게 만들 수 없다는 뜻이므로
                // 윈도우의 왼쪽 포인터(left)를 증가시켜 윈도우 크기를 줄인다.
                count[s.charAt(left) - 'A']--; // left pointer의 문자 카운트 감소
                left++;
            }

            result = Math.max(result, right - left + 1);
        }


        return result;
    }
}
// Time Complexity: O(n)
// Space Complexity: O(1)
