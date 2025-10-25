class Solution {
    public int[] countBits(int n) {
        int[] bitCountArr = new int[n+1];

        for (int i = 1; i <= n; ++i) {
            bitCountArr[i] = bitCountArr[i/2] + (i & 1);
        }

        return bitCountArr;
    }
}
