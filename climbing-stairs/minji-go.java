/*
    Problem: https://leetcode.com/problems/climbing-stairs/
    Description: how many distinct ways can you climb to the top, if you can either climb 1 or 2 steps
    Concept: Dynamic Programming, Memoization, Recursion, Math, Array, Iterator, Combinatorics ...
    Time Complexity: O(n), Runtime: 0ms
    Space Complexity: O(1), Memory: 40.63MB
*/
class Solution {
    public int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;

        int prev=1, cur=2;
        for(int i=3; i<=n; i++){
            int next=prev+cur;
            prev=cur;
            cur=next;
        }
        return cur;
    }
}
