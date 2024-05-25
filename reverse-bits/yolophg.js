// Time Complexity: O(1)
// Space Complexity: O(1)

var reverseBits = function(n) {
    let result = 0;
    // iterate 32 times since it's a 32-bit integer.
    for (let i = 0; i < 32; i++) {
        // shift the result to the left by 1 bit and OR it with the least significant bit of n.
        result = (result << 1) | (n & 1);
        // right shift n by 1 to consider the next bit.
        n >>>= 1;
    }
    
    // convert to unsigned integer.
    return result >>> 0; 
};
