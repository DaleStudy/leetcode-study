class Solution {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];
        int i = 1;
        
        for (int num = 1; num <= n; num++) {
            if (i << 1 == num) {
                i = num;
            }
            bits[num] = 1 + bits[num - i];
        }
        
        return bits;
    }
}
