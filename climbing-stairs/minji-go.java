/**
 * <a href="https://leetcode.com/problems/climbing-stairs/">week02-2.climbing-stairs</a>
 * <li> Description: how many distinct ways can you climb to the top, if you can either climb 1 or 2 steps  </li>
 * <li> Concept: Dynamic Programming, Memoization, Recursion, Math, Array, Iterator, Combinatorics ...      </li>
 * <li> Time Complexity: O(n), Runtime: 0ms     </li>
 * <li> Space Complexity: O(1), Memory: 40.39MB </li>
 */

class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int prev = 1;
        int curr = 2;

        for (int i = 3; i <= n; i++) {
            int next = prev + curr;
            prev = curr;
            curr = next;
        }

        return curr;
    }
}
