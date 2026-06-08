class Solution {
    public int[] countBits(int n) {
        /**
        1.문제: n까지의 수를 2진수로 변경 후 1의 개수를 배열에 저장
        2.constraints: 최소 O(n logn) 으로 풀 것
        3.solutions:
        - 0~n까지 for문 돌면서 2진수로 변환 -> 변환하면서 1개수 count -> 배열에 저장
        - time complexity: O(n log n) , space: O(n)
         */

         int[] answer = new int[n+1];

         for(int i = 0; i <= n; i++) {
            if(i == 0 || i == 1) {
                answer[i] = i;
                continue;
            }
            int count = getNumOfOne(i);
            answer[i] = count;
         }
         return answer;
    }

    int getNumOfOne(int n) {
        int cnt = 0;
        String binary = Integer.toBinaryString(n);

        for(char c: binary.toCharArray()) {
            if(c == '1') {
                cnt++;
            }
        }
        return cnt;
    }

}
