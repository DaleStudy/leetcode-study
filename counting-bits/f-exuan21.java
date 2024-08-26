//time : O(n)
//space : O(n)

class Solution {

    // f(n) = f(n >> 1) + (n & 1)

    public int[] countBits(int n) {
        int[] answer = new int[n + 1];

        answer[0] = 0;
        for(int i = 1; i <= n; i++) {
            answer[i] = answer[i >> 1] + (i & 1);
        }

        return answer;
    }
}
