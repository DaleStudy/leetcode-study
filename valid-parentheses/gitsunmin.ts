/**
 * https://leetcode.com/problems/valid-parentheses/
 * time complexity : O(n)
 * space complexity : O(n)
 */

type OpeningBracket = '(' | '[' | '{';
type ClosingBracket = ')' | ']' | '}';

const isEmpty = (stack: OpeningBracket[]): boolean => stack.length === 0;

function isValid(s: string): boolean {
    const m = new Map<string, ClosingBracket>([
        ['(', ')'],
        ['[', ']'],
        ['{', '}']
    ]);
    const stack: OpeningBracket[] = [];

    for (const c of s) {
        if (m.has(c)) stack.push(c as OpeningBracket);
        else if (isEmpty(stack) || c !== m.get(stack.pop() as OpeningBracket)) return false;
    }
    return isEmpty(stack);
};
