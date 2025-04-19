class Solution {
    public int hammingWeight(int n) {
        int answer = 0;
        while (n > 0) {
            answer += n & 1;
            n >>= 1;
        }

        return answer;
    }
}

/*
class Solution {
    public int hammingWeight(int n) {
        return Integer.toBinaryString(n).replace("0", "").length();
    }
}
*/
