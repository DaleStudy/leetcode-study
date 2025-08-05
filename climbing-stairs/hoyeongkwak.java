/*
Time Complexity : O(n)
Space Complexity : O(1)
*/
class Solution {
    public int climbStairs(int n) {
        if (n < 3) return n;
        int prev = 1;
        int curr = 2;

        for(int i = 0; i < n - 2; i++) {
            int temp = prev;
            prev = curr;
            curr = temp + curr;
        }
        return curr;
    }
}
