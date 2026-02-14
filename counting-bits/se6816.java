class Solution {
    public int[] countBits(int n) {
        int[] list = new int[n + 1];
        for(int i = 0; i <= n; i++) {
            list[i] = Integer.bitCount(i);
        }
        return list;
    }
}
