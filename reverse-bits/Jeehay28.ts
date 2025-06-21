// TC: O(1)
// SC: O(1)
function reverseBits(n: number): number {
  let stack: number[] = [];

  while (stack.length < 32) {
    stack.push(n % 2);
    n = Math.floor(n / 2);
  }

  let output: number = 0;
  let scale: number = 1;

  while (stack.length > 0) {
    output += stack.pop()! * scale;
    scale *= 2;
  }

  return output;
}

// TC: O(1)
// SC: O(1)
/*
function reverseBits(n: number): number {
  let result = 0;

  for (let i = 0; i < 32; i++) {
    let bit = n & 1;
    result = (result << 1) | bit;
    n = n >>> 1;
  }

  return result >>> 0;
} 
*/

/*
n & 1
- get last bit
- equivalent to n % 2 for non-negative integer

n << 1
- left shift (multiply by 2)

n >>> 1
- Unsigned right shift (divide by 2)
- ignores sign

n >>> 0
- no shift, just cast to unsigned
   
const signed = -1;             // Binary: 11111111111111111111111111111111
const unsigned = signed >>> 0; // 4294967295

JavaScript/TypeScript only has one number type — a 64-bit float. itwise operations use 32-bit signed integers.
    To return a 32-bit unsigned integer, use >>> 0 on the result.
    
    🔧 Bitwise Operations in JavaScript — Summary
    1. Bitwise operations in JavaScript (&, |, ^, ~, <<, >>, >>>) are always performed on 32-bit signed integers.

    2. Internally:
        - JavaScript converts your number into a 32-bit signed integer
        - Performs the bitwise operation
        - Then converts it back into a regular 64-bit number (JavaScript's only number type)

    3. If you need the result as a 32-bit unsigned integer (like for LeetCode problems dealing with uint32):
        - Use >>> 0 at the end of your result
        - This forces the result to be treated as an unsigned 32-bit integer
*/
