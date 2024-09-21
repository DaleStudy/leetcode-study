// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if (s.length % 2 !== 0) return false

   const stack = []

    const opener = {
        "(" : ")",
        "{": "}",
        "[": "]"
    }

    for (let i = 0 ; i < s.length; i++) {
        if (s[i] in opener) {
            stack.push(s[i]);
        } else {
            if (opener[stack.at(-1)] === s[i]) {
                stack.pop()
            } else {
                return false
            }
        }
    }


    return stack.length === 0
};

console.log(isValid("()")); // true
console.log(isValid("()[]{}")); // true
console.log(isValid("(]")); // false
console.log(isValid("([])")); // true
console.log(isValid("([}}])")); // true
