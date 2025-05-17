/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = []

    const pair = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for (let item of s) {
        // 여는 괄호
        if(item === '(' || item === '{' || item === '[') {
            stack.push(item)
        // stack길이가 0 or 닫는 괄호 케이스
        } else if (stack.length === 0 || stack.pop() !== pair[item]) {
            return false
        }
    }

    return stack.length === 0
};
