/**
 * [Problem]: [20] Valid Parentheses
 * (https://leetcode.com/problems/valid-parentheses/)
 */
function isValid(s: string): boolean {
    //시간복잡도: O(n)
    //공간복잡도: O(n)
    const stack: string[] = [];
    const pairs: Record<string, string> = { ")": "(", "}": "{", "]": "[" };

    for (const char of s) {
        if (["(", "{", "["].includes(char)) {
            stack.push(char);
        } else {
            if (stack.pop() !== pairs[char]) return false;
        }
    }

    return stack.length === 0;
}
