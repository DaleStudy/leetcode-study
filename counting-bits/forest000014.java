/*
# Time Complexity: O(n)
# Space Complexity: O(1)
*/
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            int x = i;
            while (x > 0) {
                ans[i] += (x & 1);
                x >>= 1;
            }
        }

        return ans;
    }
}
