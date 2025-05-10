/**
 * 주어진 문자열의 괄호 쌍이 알맞는지 반환하는 함수
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
    const stack = [];
    const pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for (const bracket of s) {
        if (bracket in pairs) {
            stack.push(bracket);
            continue;
        } 
        
        const popped = stack.pop();
        if (bracket !== pairs[popped]) {
            return false;
        }
    }

    return stack.length === 0;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
