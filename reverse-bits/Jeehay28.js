/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */

// Time Complexity: O(1)
// Space Complexity: O(1)

var reverseBits = function (n) {

    let stack = [];
    let num = n;

    for (let i = 0; i < 32; i++) {

        stack.push(num % 2);
        num = Math.floor(num / 2);
    }

    stack = stack.reverse();


    let result = 0;

    for (let i = 0; i < 32; i++) {

        result += stack[i] * Math.pow(2, i);

    }

    return result;

};


