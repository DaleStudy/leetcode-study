/**
 * [Problem]: [659] Encode and Decode Strings
 *
 * (https://www.lintcode.com/problem/659/)
 */

//시간복잡도 O(n)
//공간복잡도 O(1)

function encode(strs: string[]): string {
    return strs.join("😄");
}
function decode(s: string): string[] {
    return s.split("😄");
}

// 시간복잡도: O(n)
// 공간복잡도: O(n)
function encode(strs: string[]): string {
    return strs.map((str) => `${str.length}:${str}`).join("");
}

// 시간복잡도: O(n)
// 공간복잡도: O(n)
function decode(str: string): string[] {
    const result: string[] = [];
    let index = 0;
    while (index < str.length) {
        const separatorIndex = str.indexOf(":", index);
        const length = +str.slice(index, separatorIndex);
        const endIndex = separatorIndex + 1 + length;

        result.push(str.slice(separatorIndex + 1, endIndex));
        index = endIndex;
    }
    return result;
}
