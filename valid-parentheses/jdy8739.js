/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];

    for (let i=0; i<s.length; i++) {
        const cur = s[i];

        if (cur === '(' || cur === '[' || cur === '{') {
            stack.push(cur);
        } else {
            const topOfStack = stack[stack.length - 1];

            const caseA = topOfStack === '(' && cur === ')';
            const caseB = topOfStack === '[' && cur === ']';
            const caseC = topOfStack === '{' && cur === '}';

            if (caseA || caseB || caseC) {
                stack.pop();
            } else {
                return false;
            }
        }
    }

    return stack.length === 0;
};

