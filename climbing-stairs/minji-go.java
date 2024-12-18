/*
    Problem: https://leetcode.com/problems/climbing-stairs/
    Description: how many distinct ways can you climb to the top, if you can either climb 1 or 2 steps
    Concept: Dynamic Programming, Memoization, Recursion, Math, Array, Iterator, Combinatorics ...
    Time Complexity: O(n), Runtime: 0ms
    Space Complexity: O(1), Memory: 40.51MB
*/
class Solution {
    public int climbStairs(int n) {
        int step1=1, step2=2;
        for(int i=3; i<n; i++){
            int step3=step1+step2;
            step1=step2;
            step2=step3;
        }
        return n==1?step1:step2;
    }
}
