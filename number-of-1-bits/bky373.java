/**
 * https://leetcode.com/problems/number-of-1-bits/
 *
 * time: O(log n)
 * space: O(1)
 */
class Solution {

    public int hammingWeight(int n) {
        int cnt = 0;
        while (n != 0) {
            cnt++;
            n &= (n - 1);
        }
        return cnt;
    }
}
