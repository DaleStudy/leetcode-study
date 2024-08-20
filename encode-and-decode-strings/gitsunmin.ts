/**
 * https://www.lintcode.com/problem/659/
 * time complexity : O(n)
 * space complexity : O(n)
 * ! emoji는 입력에서 제외한다.
 */

function encode(input: Array<string>): string {
    return input.join("😀");
}

function decode(input: string): Array<string> {
    return input.split("😀");
}
