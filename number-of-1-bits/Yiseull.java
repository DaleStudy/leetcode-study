class Solution {
    public int hammingWeight(int n) {
        // return Integer.bitCount(n);

        int answer = 0;
        while (n != 0) {
            n &= n-1;
            answer++;
        }
        return answer;
    }
}
