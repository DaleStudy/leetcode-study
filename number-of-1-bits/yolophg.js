// Time Complexity: O(log n)
// Space Complexity: O(1)

var hammingWeight = function(n) {
    let count = 0;
    while (n !== 0) {
        // add 1 to count if the last bit is 1.
        count += n & 1; 
        // unsigned right shift to process the next bit.
        n = n >>> 1;    
    }
    
    return count;
};
