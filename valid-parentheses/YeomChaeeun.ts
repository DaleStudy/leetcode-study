/**
 * valid-parentheses
 * 괄호의 열고 닫히는 짝을 확인하는 알고리즘
 * Stack(LIFO) 데이터 구조 사용
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param s
 */
function isValid(s: string): boolean {

    // 접근 1 - {}, (), [] 가 포함되는지 보고 replace문으로 단순하게 풀어봄..
    // while (s.includes("{}") || s.includes("()") || s.includes("[]")) {
    //     s = s.replace("{}", "");
    //     s = s.replace("()", "");
    //     s = s.replace("[]", "");
    // }
    // return s === '';

    // 접근 2 - leetCode의 hint를 보고 stack 을 적용
    const stack: string[] = []
    const pairs: {[key: string]: string} = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    for (const char of s) {
        if (!pairs[char]) {
            // 여는 괄호 저장
            stack.push(char)
        } else {
             // 닫는 괄호와 매칭 확인
            if (stack.pop() !== pairs[char]) {
                return false
            }
        }
    }

    return stack.length === 0
}

