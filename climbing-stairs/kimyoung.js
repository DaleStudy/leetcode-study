// found a pattern where the result is the addition of two previous elements,
// but not sure if this is the expected answer
var climbStairs = function (n) { 
    let arr = new Array(n).fill(1);
    for (let i = 2; i <= n; i++) {
        arr[i] = arr[i - 2] + arr[i - 1];
    }
    return n === 1 ? 1 : arr[n];
};

// time - O(n) iterate up to n times
// space - O(n) creates an array upto n elements
