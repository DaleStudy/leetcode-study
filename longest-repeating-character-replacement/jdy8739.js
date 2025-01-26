/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let start = 0;
    let end = 0;
    let maxLength = 0;
    let maxCountOfChar = 0;

    const charMap = new Map();
    charMap.set(s[end], 1);

    while (end < s.length) {
        maxCountOfChar = Math.max(maxCountOfChar, charMap.get(s[end]));

        const currLength = end - start + 1;

        const countOfOthers = currLength - maxCountOfChar;

        // 현재 문자열의 길이에서 가장 많이 나오는 문자열의 수를 뺸 값인 countOfOthers가
        // k보다 작으면 현재 문자열에서 start번 째 문자의 수를 map에서 감소시키고 star의 값을 증가시킨다.
        if (countOfOthers > k) {            
            const startCharCount = charMap.get(s[start]);
            charMap.set(s[start], startCharCount - 1);

            start++;
        } else {
            // countOfOthers가 k보다 같거나 작을 경우 k번 문자를 바꾸는 것으로 현재 문자열을 모두 하나의 문자로 통일시킬 수 있다는 것으로
            // 현재 문자열에서 end번 째 문자의 수를 map에서 증가시킨다.
            // 이후 end의 값을 증가시킨다.
            end++;
            
            const endCharCount = charMap.get(s[end]);

            if (endCharCount) {
                charMap.set(s[end], endCharCount + 1);
            } else {
                charMap.set(s[end], 1);
            }
        }

        maxLength = Math.max(maxLength, Math.min(maxCountOfChar + k, currLength));
    }

    return maxLength;
};

// 시간복잡도 O(n) -> 슬라이딩 윈도우기법으로 최대 1번 순회한다.
// 공간복잡도 O(1) -> map의 크기는 알파벳의 갯수인 최대 26개이다.
