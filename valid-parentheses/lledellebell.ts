/***
 * 
 * @problem
 * - 여는 괄호와 닫는 괄호가 올바르게 짝을 이루는지 확인하는 문제입니다.
 * 
 * @constraints
 * - 문자열은 오직 '(', ')', '{', '}', '[', ']' 문자로만 구성됩니다.
 * - 문자열의 길이는 0 이상 10^4 이하입니다.
 * 
 * @example
 * - 입력: "()"
 *   출력: true
 * - 입력: "(){}"
 *   출력: true
 * - 입력: "(]"
 *   출력: false
 * - 입력: "([)]"
 *   출력: false
 * - 입력: "{}"
 *   출력: true
 * 
 * @description
 * - 여는 괄호는 스택에 추가하고, 닫는 괄호가 나오면 스택의 맨 위 요소(가장 최근에 추가된 여는 괄호)와 비교합니다.
 * - 닫는 괄호와 스택의 맨 위 요소가 짝을 이루지 않으면 유효하지 않은 문자열로 판단합니다.
 * - 문자열을 모두 순회한 후 스택이 비어 있으면 유효한 괄호 문자열입니다.
 * 
 * @complexity
 * - 시간 복잡도: O(n)
 *   문자열을 한 번만 순회하므로 시간 복잡도는 O(n)입니다.
 * - 공간 복잡도: O(n)
 *   스택에 저장되는 여는 괄호의 최대 개수는 문자열 길이에 비례하므로 공간 복잡도는 O(n)입니다.
 * 
 */
function isValid(s: string): boolean {
    // 괄호 쌍을 저장하는 Map 생성
    const map = new Map<string, string>([
        [')', '('],
        ['}', '{'],
        [']', '[']
    ]);

    // 스택 초기화
    const stack: string[] = [];

    // 문자열을 순회
    for (const char of s) {
        if (map.has(char)) {
            // 닫는 괄호일 경우 스택에서 pop하여 비교
            const topElement = stack.length > 0 ? stack.pop() : undefined;
            if (topElement !== map.get(char)) {
                return false; // 올바르지 않은 경우
            }
        } else {
            // 여는 괄호일 경우 스택에 push
            stack.push(char);
        }
    }

    // 스택이 비어 있으면 유효한 괄호(모든 여는 괄호가 닫는 괄호와 짝을 이룸)
    return stack.length === 0;
}

console.log(isValid("()")); // true
console.log(isValid("(){}")); // true
console.log(isValid("(]")); // false
console.log(isValid("([)]")); // false
console.log(isValid("{[]}")); // true
