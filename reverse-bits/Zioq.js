/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let result = 0; //Initial value
    for (let i=0; i < 32; i++) { //The loop iterates 32 times, as the input n is a 32-bit unsigned integer
        result = (result << 1) | (n & 1); // Shift the result to the left by 1 bit OR it with the least significant bit of n.
        n >>= 1; // Shifts the bits of n one place to the right, effectively "removing" the processed LSB.
    }
    return result >>> 0;    
};
/* 
    Time Complexity: O(1), because we always loop exactly 32 times, regardless of the input.
    Space Complexity: O(1), because we use a constant amount of space.
*/



