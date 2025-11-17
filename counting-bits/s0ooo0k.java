class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            arr[i] = arr[i >> 1] + (i & 1);
        }
        
        return arr;
    }
}

