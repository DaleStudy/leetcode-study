// Time Complexity: O(n)
// Space Complexity: O(n)

var countBits = function(n) {
    // initialize an array to hold the result.
    let ans = new Array(n + 1).fill(0);
    
    // iterate through all numbers from 1 to n.
    for (let i = 1; i <= n; i++) {
        ans[i] = ans[i >> 1] + (i & 1);
    }
    return ans;
};
