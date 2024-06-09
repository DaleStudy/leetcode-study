/**
 * https://leetcode.com/problems/counting-bits/
 *
 * time: O(n * log n)
 * space: O(1)
 */
class Solution {

    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int x = i;
            int cnt = 0;
            while (x != 0) {
                cnt++;
                x &= (x - 1);
            }
            ans[i] = cnt;
        }
        return ans;
    }
}

