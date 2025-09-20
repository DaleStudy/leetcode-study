/**
 * @param {string} s
 * @return {number}
 *
 * 풀이 방법 1
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

/**
 * 풀이 방법 2
 *
 * 1. dfs를 통해 모든 경우의 수를 구한다.
 * 2. isPalindrome 함수를 통해 팰린드롬인지 확인한다.
 *
 * 복잡성
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
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

    function dfs(startIdx) {
        // 모든 시작점 탐색 완료
        if (startIdx === s.length) return;

        // 현재 시작점에서 가능한 모든 끝점 확인
        for (let end = startIdx; end < s.length; end++) {
            const sub = s.slice(startIdx, end + 1);
            if (isPalindrome(sub)) {
                count++;
            }
        }

        // 다음 시작점으로 이동
        dfs(startIdx + 1);
    }

    dfs(0);
    return count;
};
