class Solution {
    public int characterReplacement(String s, int k) {
        /**
        1.problem: k번 특정 문자를 골라서 바꿀 수 있다. 이때 same letter 로 이루어진 가장 긴 substring 의 길이을 구하라.
        2.constraints
        - s.length min = 1, max = 10^5
        - k.length min = 0, max = s.length
        3.solution
        - sliding window: time O(n), space O(1)
         */

        int[] table = new int[26];
        int n = s.length();
        int maxFreq = 0;
        int maxLen = 0;
        int left = 0;

        for(int right = 0; right < n; right++) {
            //1.right 확장 -> count 증가
            int currentChar = s.charAt(right) - 'A';
            table[currentChar]++;

            //2.maxFreq update
            maxFreq = Math.max(maxFreq, table[currentChar]);

            //3.조건 깨지면 left 이동하면서 count--
            //바꿔야하는 문자 개수가 k 보다 큰 경우
            if((right - left + 1 - maxFreq) > k) {
                int idx = s.charAt(left) - 'A';
                table[idx]--;
                left++;
            }

            //4.maxLen update
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
