class Solution {
    public int hammingWeight(int n) {
        int result = 1;
        if(n <= 2) {
            return result;
        }
        while (true) {
            if (n % 2 == 1) {
                result++;
            }
            n /= 2;
            if(n <= 2) {
                break;
            }
        }
        return result;
    }
}
