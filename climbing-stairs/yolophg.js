// Time complexity : O(n)
// Space complexity : O(n)

var climbStairs = function(n) {
    // create a memoization object to store results.
    const memo = {};
    
    // recursive function to calculate the number of ways to climb n steps.
    function climb(n) {
        // if n is 1 or 2, there's only one way to climb or two ways.
        if (n <= 2) return n;
        
        // if the result for n is already computed, return it from memo.
        if (memo[n]) return memo[n];
        
        // otherwise, compute the result recursively.
        memo[n] = climb(n - 1) + climb(n - 2);
        return memo[n];
    }
    
    return climb(n);    
};
