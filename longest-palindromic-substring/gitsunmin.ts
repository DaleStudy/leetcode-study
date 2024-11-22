/**
 * https://leetcode.com/problems/longest-palindromic-substring/
 * time complexity : O(n)
 * space complexity : O(n^2)
 */

function findPalindromeAroundCenter(s: string, leftIndex: number, rightIndex: number): [number, number] {
    while (leftIndex >= 0 && rightIndex < s.length && s[leftIndex] === s[rightIndex]) {
        leftIndex--; // 왼쪽으로 확장
        rightIndex++; // 오른쪽으로 확장
    }

    // 팰린드롬의 시작과 끝 인덱스 반환
    return [leftIndex + 1, rightIndex - 1];
}

function longestPalindrome(s: string): string {
    if (s.length <= 1) return s;

    let longestPalindromeStartIndex = 0;
    let longestPalindromeLength = 0;

    for (let centerIndex = 0; centerIndex < s.length; centerIndex++) {
        // 홀수 길이 팰린드롬 확인
        const [oddStart, oddEnd] = findPalindromeAroundCenter(s, centerIndex, centerIndex);
        const oddLength = oddEnd - oddStart + 1;

        if (oddLength > longestPalindromeLength) {
            longestPalindromeStartIndex = oddStart;
            longestPalindromeLength = oddLength;
        }

        // 짝수 길이 팰린드롬 확인
        const [evenStart, evenEnd] = findPalindromeAroundCenter(s, centerIndex, centerIndex + 1);
        const evenLength = evenEnd - evenStart + 1;

        if (evenLength > longestPalindromeLength) {
            longestPalindromeStartIndex = evenStart;
            longestPalindromeLength = evenLength;
        }
    }

    // 가장 긴 팰린드롬 부분 문자열 반환
    return s.substring(longestPalindromeStartIndex, longestPalindromeStartIndex + longestPalindromeLength);
}
