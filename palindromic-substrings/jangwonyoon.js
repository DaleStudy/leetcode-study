/**
 * @param {string} s
 * @return {number}
 *
 * 풀이 방법
 *
 * 1. brute force 를 사용해서 모든 경우의 수를 구한다.
 * 2. 투포인터를 통해 isPalindrome 을 확인한다.
 *
 * 복잡성
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

/**
 * isPalindrome 함수
 */
function isPalindrome(s) {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }

    return true;
}

var countSubstrings = function(s) {
    let count = 0;

    // 모든 경우의 수를 구한다.
    for (let start = 0; start < s.length; start++) {
        for (let end = start; end < s.length; end++) {
            const subStr = s.slice(start, end + 1);

            // isPalindrome 함수를 통해 팰린드롬인지 확인한다.
            if (isPalindrome(subStr)) {
                count++;
            }
        }
    }

    return count;
};
