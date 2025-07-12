/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function(s) {
    let substr = '';

    for (let i = 0; i < s.length; i++) {
        const oddStr = getCurrentLongestPalindrome(i, i); // s[i] 기준 양옆으로 뻗어나감 => length는 항상 홀수
        const evenStr = getCurrentLongestPalindrome(i, i+1); // s[i] + s[i+1] 기준 양옆으로 => length는 항상 짝수
        
        if (substr.length < oddStr.length) substr = oddStr;
        if (substr.length < evenStr.length) substr = evenStr;
    }
  
    // 기준 문자열을 포함하면서 가장 긴 팰린드롬을 찾아 반환하는 함수 (기준 문자열: s.slice(l, r + 1))
    const getCurrentLongestPalindrome = function (l, r) {
        while (0 <= l && r < s.length && s[l] === s[r]) {
            l--;
            r++;
        }

        return s.slice(l+1, r);
    }

    return substr;
};

// 시간복잡도: O(n^2)
// 공간복잡도: O(s) (s: substr.length)
