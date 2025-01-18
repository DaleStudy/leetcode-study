/**
 * 주어진 문자열 s가 유효한 괄호 문자열인지 확인.
 * @param {string} s - 입력 문자열 (괄호만 포함됨)
 * @returns {boolean} - 유효한 괄호 문자열이면 true, 아니면 false
 *
 * 시간 복잡도: O(n)
 * - 문자열의 길이 n만큼 한 번씩 순회하며, 각 문자에 대해 고정된 연산(스택 조작)을 수행.
 *
 * 공간 복잡도: O(n)
 * - 최악의 경우 스택에 여는 괄호 n개를 저장해야 하므로 O(n)의 추가 메모리가 필요합니다.
 */
function isValid(s: string): boolean {
    if (s.length % 2 !== 0) return false;
    if (s === '') return true;

    const bracketSets: Record<string, string> = { '(': ')', '{': '}', '[': ']' };
    const bracketStack: string[] = [];

    for (const char of s) {
        if (char in bracketSets) {
            // 여는 괄호인 경우 스택에 추가
            bracketStack.push(char);
        } else {
            // 닫는 괄호인 경우 스택에서 마지막 여는 괄호를 꺼냄
            const lastOpeningBracket = bracketStack.pop();
            // 유효하지 않은 괄호 조합인 경우
            if (bracketSets[lastOpeningBracket!] !== char) {
                return false;
            }
        }
    }

    // 스택이 비어있으면 모든 괄호가 유효
    return bracketStack.length === 0;
}
